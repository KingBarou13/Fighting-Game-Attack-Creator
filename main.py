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
                                   f"  Charge Time        : {properties['chargeTime']} frames\n"
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

def get_input_list(prompt, allow_multiple=False):
    user_input = input(prompt)
    if allow_multiple:
        return [int(x.strip()) for x in user_input.split(",")]
    return int(user_input.strip())

def create_attack():
    print("Define your attack:\n")

    attackStrength = input("Enter attack strength (e.g., Light, Medium, Heavy): ")
    attackInput = input("Enter attack input (e.g., 5L, 2M): ")
    damage_input = get_input_list("Enter damage (comma-separated for multi-hit): ", True)
    attackHeight = input("Enter attack height (e.g., High, Mid, Low): ")
    startupFrames_input = get_input_list("Enter startup frames (comma-separated for multi-hit): ", True)
    activeFrames_input = get_input_list("Enter active frames (comma-separated for multi-hit): ", True)
    recoveryFrames = get_input_list("Enter recovery frames: ")
    invulFrames = get_input_list("Enter invul frames: ")
    hitstun_input = get_input_list("Enter hitstun (comma-separated for multi-hit): ", True)
    blockstun_input = get_input_list("Enter blockstun (comma-separated for multi-hit): ", True)
    meterGain = get_input_list("Enter meter gain: ")
    counterProperties = input("Enter counter properties (comma-separated, leave blank if none): ").split(",")
    counterProperties = [x.strip() for x in counterProperties] if counterProperties[0] else []
    range_input = get_input_list("Enter range: ")
    cancelOptions = input("Enter cancel options (comma-separated, leave blank if none): ").split(",")
    cancelOptions = [x.strip() for x in cancelOptions] if cancelOptions[0] else []
    verticalKnockback_input = get_input_list("Enter vertical knockback (comma-separated for multi-hit): ", True)
    horizontalKnockback_input = get_input_list("Enter horizontal knockback (comma-separated for multi-hit): ", True)

    chargeLevels = {}
    has_charge_levels = input("Does this move have charge levels? (yes/no): ").strip().lower()
    if has_charge_levels == "yes":
        num_charge_levels = get_input_list("How many charge levels? ")
        for level in range(1, num_charge_levels + 1):
            print(f"\nDefine properties for Charge Level {level}:\n")
            chargeTime = get_input_list("  Enter charge time (frames): ")
            damage = get_input_list("  Enter damage (comma-separated for multi-hit): ", True)
            startupFrames = get_input_list("  Enter startup frames (comma-separated for multi-hit): ", True)
            activeFrames = get_input_list("  Enter active frames (comma-separated for multi-hit): ", True)
            recoveryFrames = get_input_list("  Enter recovery frames: ")
            hitstun = get_input_list("  Enter hitstun (comma-separated for multi-hit): ", True)
            blockstun = get_input_list("  Enter blockstun (comma-separated for multi-hit): ", True)
            verticalKnockback = get_input_list("  Enter vertical knockback (comma-separated for multi-hit): ", True)
            horizontalKnockback = get_input_list("  Enter horizontal knockback (comma-separated for multi-hit): ", True)

            chargeLevels[level] = {
                "chargeTime": chargeTime,
                "damage": damage,
                "startupFrames": startupFrames,
                "activeFrames": activeFrames,
                "recoveryFrames": recoveryFrames,
                "hitstun": hitstun,
                "blockstun": blockstun,
                "verticalKnockback": verticalKnockback,
                "horizontalKnockback": horizontalKnockback
            }

    attack = Attack(
        attackStrength,
        attackInput,
        damage_input,
        attackHeight,
        startupFrames_input,
        activeFrames_input,
        recoveryFrames,
        invulFrames,
        hitstun_input,
        blockstun_input,
        meterGain,
        counterProperties,
        range_input,
        cancelOptions,
        verticalKnockback_input,
        horizontalKnockback_input,
        chargeLevels
    )

    print(attack)
    attack.calculateFrameAdvantage()
    attack.calculateHitAdvantage()

if __name__ == "__main__":
    create_attack()
