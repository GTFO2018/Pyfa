# subsystemBonusMinmatarDefensiveArmorResistance
#
# Used by:
# Subsystem: Loki Defensive - Adaptive Augmenter
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Defensive Systems").level
    for type in ("Em", "Explosive", "Kinetic", "Thermal"):
        fit.ship.boostItemAttr("armor{0}DamageResonance".format(type),
                               module.getModifiedItemAttr("subsystemBonusMinmatarDefensive") * level)
