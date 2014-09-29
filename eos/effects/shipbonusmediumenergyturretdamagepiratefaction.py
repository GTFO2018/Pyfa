# shipBonusMediumEnergyTurretDamagePirateFaction
#
# Used by:
# Ship: Ashimmu
# Ship: Gnosis
# Ship: Phantasm
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusPirateFaction"))
