def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    prev_time = 0

    for attack_time, damage in attacks:
        gap = attack_time - prev_time - 1
        health = min(health + (gap * x) + (gap // t) * y, max_health)
        health -= damage
        if health <= 0:
            return -1
        prev_time = attack_time

    return health