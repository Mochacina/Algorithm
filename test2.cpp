#include <...>

EXEC SQL INCLUDE SQLCA ;

oraProc::oraProc()
{
	memset(m_szSid, 0x00, ORACLE_CON_SIZE);
	memset(m_szUser, 0x00, ORACLE_CON_SIZE);
	memset(m_szPasswd, 0x00, ORACLE_CON_SIZE);
	m_bEstablished = false;
	m_nReadflag = 0;
}

oraProc::~oraProc()
{
	EXEC SQL DECLARE DB_CONNECTION DATABASE;
	EXEC SQL AT DB_CONNECTION COMMIT WORK RELEASE;
}


// 내부 DB 접속
bool oraProc::connect( const char  *user,
		const char   *passwd,
		const char   *sid)
{
	strcpy(m_szUser, user);
	strcpy(m_szPasswd, passwd);
	strcpy(m_szSid, sid);

	EXEC SQL BEGIN DECLARE SECTION;
		varchar vc_sysdate[128];
		varchar m_szCon_script[256];

		char user1[20];
		char passwd1[20];
		char sid1[20];

	EXEC SQL END DECLARE SECTION;

	if (m_nReadflag == 0)
	{
		sprintf((char *)m_szCon_script.arr, "%s/%s@%s", m_szUser, m_szPasswd, m_szSid);
		m_szCon_script.len = strlen((char *)m_szCon_script.arr);
		m_nReadflag = 1;
	}

	strcpy(user1, user);
	strcpy(passwd1, passwd);
	strcpy(sid1, sid);

CONNECT_DB:

	if (!m_bEstablished)
	{
		//log(5, "Try to connect oracle : %s %s %s\n", user, passwd, sid);
		log(5, "Try to connect oracle \n");

		EXEC SQL CONNECT :user1 IDENTIFIED BY :passwd1 AT DB_CONNECTION USING :sid1;

		if(sqlca.sqlcode != 0 )
		{
			log(3, "Oracle DB Connection fail... %s (%d)", (char *)m_szCon_script.arr, sqlca.sqlcode );
			
			m_bEstablished = false;
			return false;
		}
		else
		{
			log(7, "Oracle DB Connection success...");
			
			m_bEstablished = true;
			return true;
		}
	}
	else
	{
		/* 실제로 연결되어 있는 지를 select하여 판정한다. */
#if 1

		EXEC SQL AT DB_CONNECTION
			SELECT  sysdate
			INTO    :vc_sysdate
			FROM    dual;

		if(sqlca.sqlcode != 0 )
		{
			if(CheckDBCLS(sqlca.sqlcode) == 1)
			{
				/* DB Disc 상태 */
				log(7, "DB 상태 오류 발견-> 재연결 시도");
				m_bEstablished = false;
				goto CONNECT_DB;
			}
			else
			{
				log(7, "DB 기연결->Do Nothing");
			}
		}
#endif
	}

	return true;
}

bool oraProc::Reconnect()
{
	if (m_bEstablished)
		return true;

	EXEC SQL AT DB_CONNECTION COMMIT WORK RELEASE;

	m_nReadflag = 0;

	if (connect(m_szUser, m_szPasswd, m_szSid))
	{
		m_bEstablished = true;
		return true;
	}

	log(5, "DB connect Error: ");
	m_bEstablished = false;

	return false;
}

bool oraProc::Established()
{
	return m_bEstablished;
}


// Roll Back
bool oraProc::Rollback()
{
	log(7, "Oracle Rollback");

	EXEC SQL AT DB_CONNECTION ROLLBACK WORK;

	log(7, "Oracle Rollback Success... ");

	return true;
}

// Commit
bool oraProc::Commit()
{
	log(7, "Oracle Commit");

	EXEC SQL AT DB_CONNECTION COMMIT WORK;

	log(7, "Oracle Commit Success... ");

	return true;
}


int oraProc::CheckDBCLS(int SqlCode)
{
	if ( ((SqlCode >= -1017)  && (SqlCode <= -1012))    ||
			((SqlCode >= -1034)  && (SqlCode <= -1033))     ||
			((SqlCode >= -3114)  && (SqlCode <= -3113))     ||
			((SqlCode >= -12699) && (SqlCode <= -12500))    ||
			((SqlCode >= -899)   && (SqlCode <= -17))       ||
			((SqlCode >= -2111)  && (SqlCode <= -2100))     ||
			((SqlCode >= -4934)  && (SqlCode <= -4930))     ||
			((SqlCode >= -25424) && (SqlCode <= -25400))    ||
			(SqlCode == -1092)  ||
			(SqlCode == -3135)   || (SqlCode == -3134)      )
	{
		log(7, "DB Connection was released... : %d", SqlCode);
		/* DB 연결 해제 */
		m_nReadflag = 0;
		m_bEstablished = false;
		return 1;
	}
	else
	{
		log(7, "CheckDBCLS... : %d", SqlCode);
		/* 일반 장애 */
		m_nReadflag = 0;
		return 0;
	}

	EXEC SQL AT DB_CONNECTION COMMIT WORK RELEASE;
}