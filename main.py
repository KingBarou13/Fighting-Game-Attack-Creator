class Attack:
  def __init__(
      self,
      attackStrength,
      attackInput,
      damage,
      attackHeight,
      startupFrames,
      activeFrames,
      recoveryFrames,
      invulFrames,
      hitstun,
      blockstun,
      meterGain=0,
      counterProperties=None,
      range=0,
      cancelOptions=None,
  ):
      self.attackStrength = attackStrength
      self.attackInput = attackInput
      self.damage = damage
      self.attackHeight = attackHeight
      self.startupFrames = startupFrames
      self.activeFrames = activeFrames
      self.recoveryFrames = recoveryFrames
      self.invulFrames = invulFrames
      self.hitstun = hitstun
      self.blockstun = blockstun
      self.meterGain = meterGain
      self.counterProperties = counterProperties if counterProperties else []
      self.range = range
      self.cancelOptions = cancelOptions if cancelOptions else []

  def calculateFrameAdvantage(self):
      frameAdvantage = self.blockstun - self.recoveryFrames
      print(f"\nFrame Advantage Calculation:")
      print(f"Frame Advantage = {frameAdvantage}")
      if frameAdvantage > 0:
          print("Result: This move is plus on block. You get to act first.")
      elif frameAdvantage < 0:
          print("Result: This move is minus on block. Your opponent gets to act first.")
      else:
          print("Result: This move is neutral on block. You and your opponent can act at the same time.")

  def calculateHitAdvantage(self):
      hitAdvantage = self.hitstun - self.recoveryFrames
      print(f"\nHit Advantage Calculation:")
      print(f"Hit Advantage = {hitAdvantage}")
      if hitAdvantage > 0:
          print("Result: This move is plus on hit. You get to act first.")
      elif hitAdvantage < 0:
          print("Result: This move is minus on hit. Your opponent gets to act first.")
      else:
          print("Result: This move is neutral on hit. You and your opponent can act at the same time.")

  def __str__(self):
      return (
          f"\nAttack Details:\n"
          f"-----------------\n"
          f"Attack Input   : {self.attackInput}\n"
          f"Strength       : {self.attackStrength}\n"
          f"Damage         : {self.damage}\n"
          f"Height         : {self.attackHeight}\n"
          f"Startup Frames : {self.startupFrames}\n"
          f"Active Frames  : {self.activeFrames}\n"
          f"Recovery Frames: {self.recoveryFrames}\n"
          f"Invul Frames   : {self.invulFrames}\n"
          f"Hitstun        : {self.hitstun}\n"
          f"Blockstun      : {self.blockstun}\n"
          f"Meter Gain     : {self.meterGain}\n"
          f"Range          : {self.range}\n"
          f"Cancel Options : {', '.join(self.cancelOptions)}\n"
      )

print(f"\nControl Scheme (Using PS5 and Numpad Notation)\n"
   f"-----------------------------------------------\n"
   f"5                     : Neutral\n"
   f"6                     : Forward\n"
   f"4                     : Back\n"
   f"8                     : Up\n"
   f"2                     : Down\n"
   f"Light Attack          : Square\n"
   f"Medium Attack         : Triangle\n"
   f"Heavy Attack          : Cross\n"
   f"Special Attack        : Circle\n"
   )

#Example Usage
slayer5K = Attack(
  "Medium",
  "5 + Triangle",
  44,
  "Mid",
  7,
  3,
  14,
  0,
  17,
  9,
  meterGain=5,
  range=3,
  cancelOptions=["Special"],
)

print(slayer5K)
slayer5K.calculateFrameAdvantage()
slayer5K.calculateHitAdvantage()
