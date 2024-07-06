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
        verticalKnockback=0,
        horizontalKnockback=0,
        chargeLevels=None
    ):
        self.attackStrength = attackStrength
        self.attackInput = attackInput
        self.damage = damage if isinstance(damage, list) else [damage]
        self.attackHeight = attackHeight
        self.startupFrames = startupFrames if isinstance(startupFrames, list) else [startupFrames]
        self.activeFrames = activeFrames if isinstance(activeFrames, list) else [activeFrames]
        self.recoveryFrames = recoveryFrames
        self.invulFrames = invulFrames
        self.hitstun = hitstun if isinstance(hitstun, list) else [hitstun]
        self.blockstun = blockstun if isinstance(blockstun, list) else [blockstun]
        self.meterGain = meterGain
        self.counterProperties = counterProperties if counterProperties else []
        self.range = range
        self.cancelOptions = cancelOptions if cancelOptions else []
        self.verticalKnockback = verticalKnockback if isinstance(verticalKnockback, list) else [verticalKnockback]
        self.horizontalKnockback = horizontalKnockback if isinstance(horizontalKnockback, list) else [horizontalKnockback]
        self.chargeLevels = chargeLevels if chargeLevels else {}

    def calculateFrameAdvantage(self):
        if self.chargeLevels:
            for level, properties in self.chargeLevels.items():
                for i, blockstun in enumerate(properties["blockstun"]):
                    frameAdvantage = blockstun - properties["recoveryFrames"]
                    print(f"\nFrame Advantage Calculation for Charge Level {level} Hit {i+1}:")
                    print(f"Frame Advantage = {frameAdvantage}")
                    if frameAdvantage > 0:
                        print("Result: This move is plus on block. You get to act first.")
                    elif frameAdvantage < 0:
                        print("Result: This move is minus on block. Your opponent gets to act first.")
                    else:
                        print("Result: This move is neutral on block. You and your opponent can act at the same time.")
        else:
            for i, blockstun in enumerate(self.blockstun):
                frameAdvantage = blockstun - self.recoveryFrames
                print(f"\nFrame Advantage Calculation for Hit {i+1}:")
                print(f"Frame Advantage = {frameAdvantage}")
                if frameAdvantage > 0:
                    print("Result: This move is plus on block. You get to act first.")
                elif frameAdvantage < 0:
                    print("Result: This move is minus on block. Your opponent gets to act first.")
                else:
                    print("Result: This move is neutral on block. You and your opponent can act at the same time.")

    def calculateHitAdvantage(self):
        if self.chargeLevels:
            for level, properties in self.chargeLevels.items():
                for i, hitstun in enumerate(properties["hitstun"]):
                    hitAdvantage = hitstun - properties["recoveryFrames"]
                    print(f"\nHit Advantage Calculation for Charge Level {level} Hit {i+1}:")
                    print(f"Hit Advantage = {hitAdvantage}")
                    if hitAdvantage > 0:
                        print("Result: This move is plus on hit. You get to act first.")
                    elif hitAdvantage < 0:
                        print("Result: This move is minus on hit. Your opponent gets to act first.")
                    else:
                        print("Result: This move is neutral on hit. You and your opponent can act at the same time.")
        else:
            for i, hitstun in enumerate(self.hitstun):
                hitAdvantage = hitstun - self.recoveryFrames
                print(f"\nHit Advantage Calculation for Hit {i+1}:")
                print(f"Hit Advantage = {hitAdvantage}")
                if hitAdvantage > 0:
                    print("Result: This move is plus on hit. You get to act first.")
                elif hitAdvantage < 0:
                    print("Result: This move is minus on hit. Your opponent gets to act first.")
                else:
                    print("Result: This move is neutral on hit. You and your opponent can act at the same time.")

    def __str__(self):
        attack_details = (f"\nAttack Details:\n"
                          f"-----------------\n"
                          f"Attack Input       : {self.attackInput}\n"
                          f"Strength           : {self.attackStrength}\n"
                          f"Damage             : {self.damage}\n"
                          f"Height             : {self.attackHeight}\n"
                          f"Startup Frames     : {self.startupFrames}\n"
                          f"Active Frames      : {self.activeFrames}\n"
                          f"Recovery Frames    : {self.recoveryFrames}\n"
                          f"Invul Frames       : {self.invulFrames}\n"
                          f"Hitstun            : {self.hitstun}\n"
                          f"Blockstun          : {self.blockstun}\n"
                          f"Meter Gain         : {self.meterGain}\n"
                          f"Range              : {self.range}\n"
                          f"Cancel Options     : {', '.join(self.cancelOptions)}\n"
                          f"Vertical Knockback : {self.verticalKnockback}\n"
                          f"Horizontal Knockback: {self.horizontalKnockback}\n")

        if self.chargeLevels:
            charge_details = "\nCharge Levels:\n---------------"
            for level, properties in self.chargeLevels.items():
                charge_details += (f"\nCharge Level {level}:\n"
                                   f"  Damage             : {properties['damage']}\n"
                                   f"  Startup Frames     : {properties['startupFrames']}\n"
                                   f"  Active Frames      : {properties['activeFrames']}\n"
                                   f"  Recovery Frames    : {properties['recoveryFrames']}\n"
                                   f"  Hitstun            : {properties['hitstun']}\n"
                                   f"  Blockstun          : {properties['blockstun']}\n"
                                   f"  Vertical Knockback : {properties['verticalKnockback']}\n"
                                   f"  Horizontal Knockback: {properties['horizontalKnockback']}\n")
            attack_details += charge_details

        return attack_details

print(f"\nControl Scheme (Using PS5 and Numpad Notation)\n"
      f"-----------------------------------------------\n"
      f"5                        : Neutral\n"
      f"6                        : Forward\n"
      f"4                        : Back\n"
      f"8                        : Up\n"
      f"2                        : Down\n"
      f"L (Light Attack)         : Square\n"
      f"M (Medium Attack)        : Triangle\n"
      f"H (Heavy Attack)         : Cross\n"
      f"S (Special Attack)       : Circle\n")

# Single-Hitting Attack
singleHitMove = Attack(
    "Light",
    "5L",
    20,
    "Low",
    5,
    2,
    10,
    0,
    15,
    7,
    meterGain=3,
    range=2,
    cancelOptions=["Special"],
    verticalKnockback=3,
    horizontalKnockback=4
)

print(singleHitMove)
singleHitMove.calculateFrameAdvantage()
singleHitMove.calculateHitAdvantage()

# Multi-Hitting Attack
multiHitMove = Attack(
    "Heavy",
    "5H",
    [30, 40, 50],
    "Mid",
    [10, 20, 30],
    [5, 5, 5],
    18,
    0,
    [25, 30, 35],
    [15, 20, 25],
    meterGain=10,
    range=5,
    cancelOptions=["Special", "Super"],
    verticalKnockback=[6, 7, 8],
    horizontalKnockback=[9, 10, 11]
)

print(multiHitMove)
multiHitMove.calculateFrameAdvantage()
multiHitMove.calculateHitAdvantage()

# Charge Attack
chargeAttackMove = Attack(
    "Charge",
    "5S (Hold)",
    None,
    "High",
    None,
    None,
    None,
    0,
    None,
    None,
    meterGain=0,
    range=5,
    cancelOptions=["Super"],
    chargeLevels={
        "Level 1": {
            "damage": [20],
            "startupFrames": [15],
            "activeFrames": [3],
            "recoveryFrames": 12,
            "hitstun": [18],
            "blockstun": [10],
            "verticalKnockback": [4],
            "horizontalKnockback": [6]
        },
        "Level 2": {
            "damage": [40],
            "startupFrames": [25],
            "activeFrames": [4],
            "recoveryFrames": 15,
            "hitstun": [22],
            "blockstun": [12],
            "verticalKnockback": [5],
            "horizontalKnockback": [8]
        },
        "Level 3": {
            "damage": [60],
            "startupFrames": [35],
            "activeFrames": [5],
            "recoveryFrames": 18,
            "hitstun": [26],
            "blockstun": [14],
            "verticalKnockback": [6],
            "horizontalKnockback": [10]
        }
    }
)

print(chargeAttackMove)
chargeAttackMove.calculateFrameAdvantage()
chargeAttackMove.calculateHitAdvantage()
