knuts = int(input())

SICKLE_TO_KNUTS = 29
GALLEON_TO_SICKLES = 17

galleons = knuts // (GALLEON_TO_SICKLES * SICKLE_TO_KNUTS)
remaining_knuts = knuts % (GALLEON_TO_SICKLES * SICKLE_TO_KNUTS)

sickles = remaining_knuts // SICKLE_TO_KNUTS
remaining_knuts = remaining_knuts % SICKLE_TO_KNUTS

knuts = remaining_knuts

if galleons > 0:
    print(f"{galleons} галлеонов")

if sickles > 0:
    print(f"{sickles} сиклей")

if knuts > 0:
    print(f"{knuts} кнатов")
