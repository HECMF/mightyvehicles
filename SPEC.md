# Specification for Mighty Vehicles Addon

## Details
- Addon ist für Bedrock Version
- Alle Fahrzeuge sind craftbar und verwenden den `mighty:` Namespace

## Fahrzeuge (Craftbar)

### Auto (`mighty:auto`)
- 80 HP, Speed 0.4, Scale 1.2
- 4 Sitze (Fahrer + 3 Passagiere)
- Boden-Fahrzeug mit `input_ground_controlled`
- Immun gegen Fallschaden, kein Despawn
- Crafting: Iron Ingots, Redstone, Glass Pane, Copper Ingot
- Droppt 3-5 Iron Ingots, 1-2 Copper Ingots

### Flugzeug (`mighty:flugzeug`)
- 60 HP, Fly Speed 0.6, Scale 1.5
- 2 Sitze (Pilot + Passagier)
- Fliegt wie Bombardilo (`can_fly` + `movement.fly`)
- Immun gegen Fallschaden, kein Despawn
- Crafting: Iron Ingots, Copper Ingots, Redstone, Glass Pane
- Droppt 2-4 Iron Ingots, 1-2 Copper Ingots

### Mech (`mighty:mech`)
- 150 HP, Speed 0.2, Attack 15, Scale 2.0, Knockback-Resistenz 0.8
- 1 Sitz (Cockpit)
- Geritten: Spieler steuert, Spieler greift an
- Nicht geritten: Greift automatisch feindliche Mobs an (wie Iron Golem)
- Immun gegen Fallschaden + Explosion, kein Despawn
- Crafting: Iron Ingots, Redstone, Copper Ingots
- Droppt 4-6 Iron Ingots, 2-3 Copper Ingots, 1 Redstone

### Boot (`mighty:boot`)
- 40 HP, Underwater Speed 0.15, Scale 1.3
- 4 Sitze (Kapitän + 3 Passagiere)
- Schwimmt auf Wasser mit `buoyant`
- Atmet Luft und Wasser, kein Despawn
- Crafting: Oak Planks, Copper Ingot
- Droppt 4-6 Oak Planks, 1 Copper Ingot
