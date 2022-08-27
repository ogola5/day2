class Time:
  def __init__(self,hours,minutes):
    self.hours=hours
    self.minutes=minutes

  
  def addTime(t1,t2):
    t3 = Time(0,0)
    if t1.minutes+ t2.minutes>60:
      t3.hours=(t1.minutes+t2.minutes)//60
    t3.hours = t3.hours+t1.hours+t2.hours
    t3.mins=(t1.minutes + t2.minutes)%60
    return t3

  def displayTime(self):
    print("Time is",self.hours,"hours and",self.minutes,"minutes.")

  def displayMinutes(self):
    print((self.hours*60)+self.minutes)

a = Time(2,50)
b = Time(1,20)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinutes()

    