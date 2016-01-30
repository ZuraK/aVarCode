
namespace alpha
{
class GameTimeDateCore
{
	// Time stepped each tick
	float m_fTickTimeStep; // I.e 10 seconds each step

	// How often to perform tick realtime
	float m_fTimeToTick;
	
	// Time elapsed since last tick
	float m_fTimeElapsed;
	
	// What time was last pass
	float m_fTimePrevious;
	
	// What time is for current pass
	float m_fTimeCurrent;
	
	bool m_TimeState; // play, pause
	bool m_SpeedTable; // 0.25, 0.50, 0.75, 1.00, 1.25 etc, to max
	bool m_DefaultValues; // defaultvalues, hardcoded
	
	// 2016-01-07 23:56:59,983
	// Stored as longlong
	bool m_CurrentGameTime;
	bool m_GameStartTimeStamp; // longlong
	
	enum GameTimeState
	{
		Idle,
		Paused,
		Play,
	}
	
	void Update()
	{
		m_fTimeCurrent = GetCurrentTime();
		m_fTimeElapsed += m_fTimeCurrent - m_fTimePrevious;
		if(m_fTimeElapsed >= m_fTimeToTick)
		{
			DoTick();
			m_fTimeElapsed = 0;
		}
		m_fTimePrevious = m_fTimeCurrent;
	}
	
	void DoTick()
	{}
}

class GameCalendar
{
	// E Time Zone
	// S Time
	// M Time Zone
	// Etc
}
}
