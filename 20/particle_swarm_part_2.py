from collections import defaultdict

from particle_swarm_part_1 import read, update, simulate

def collisions(particles):
    positions = defaultdict(set)

    for particle in particles:
        i, position, velocity, acceleration = particle

        positions[position].add(i)

    collided = set()

    for position, ids in positions.items():
        if len(ids) > 1:
            collided.update(set(ids))
    return collided

def remove_collisions(particles, collided):

    return [particle for particle in particles if particle[0] not in collided]

def tick(particles):
    updated = [update(particle) for particle in particles]
    positions = collisions(updated)
    return remove_collisions(updated, positions)

def simulate(particles, n=1000):
    nticks = 0

    for _ in range(n):
        particles = tick(particles)
        nticks += 1

    return particles

def main():
    with open('test_case_part_2.txt', 'r') as particles_input:
        particles = read(particles_input)
        assert len(simulate(particles)) == 1

    with open('input.txt', 'r') as particles_input:
        particles = read(particles_input)
        print('Answer: ', len(simulate(particles, n=1000)))

if __name__ == '__main__':
    main()
