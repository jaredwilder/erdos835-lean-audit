# Gauge Trades vs Physical Trades

## Gauge trade

A trade whose positive and negative sides both lie inside the existing 4275-block union of the P15.

It can change which constituent system owns which blocks, but it preserves the total union and therefore preserves the same 570 holes.

The pair components from `03_PAIR_TRADE_GRAPH.md` are gauge trades.

## Physical trade

A trade whose positive side includes one or more blocks from the 570-hole set, changing the total occupied union.

Only a physical trade can change the residual q=2 graph and potentially remove the four K5 obstruction components found in the previous 30-round release.

## Exact pruning inherited from the campaign

1. One-coordinate rigidity rules out a physical escape involving only one constituent system.
2. The previous repair-radius theorem rules out completing while retaining 13,14,or15 systems from this P15: any full large set retaining members of P can retain at most 12.
3. Therefore any path from this P15 to a full large set requires simultaneous physical surgery involving at least three constituent systems.

This is the recommended search representation for the next campaign: enumerate/minimize physical trades in the incidence kernel under a mandatory hole-intersection constraint.
