import re

def read(particles_input):
    pos = re.compile(r'p=<(-?\d+),(-?\d+),(-?\d+)>')
    vel = re.compile(r'v=<(-?\d+),(-?\d+),(-?\d+)>')
    acc = re.compile(r'a=<(-?\d+),(-?\d+),(-?\d+)>')

    particles = []

    for i, row in enumerate(particles_input):

        pos_match = pos.search(row)
        px, py, pz = pos_match.group(1), pos_match.group(2), pos_match.group(3)

        vel_match = vel.search(row)
        vx, vy, vz = vel_match.group(1), vel_match.group(2), vel_match.group(3)

        acc_match = acc.search(row)
        ax, ay, az = acc_match.group(1), acc_match.group(2), acc_match.group(3)



        particles.append([
            i,
            (int(px), int(py), int(pz)),
            (int(vx), int(vy), int(vz)),
            (int(ax), int(ay), int(az))
        ])

    return particles

def update(particle):
    i, position, velocity, acceleration = particle

    px, py, pz = position
    vx, vy, vz = velocity
    ax, ay, az = acceleration

    vx += ax
    vy += ay
    vz += az

    px += vx
    py += vy
    pz += vz

    return [i, (px, py, pz), (vx, vy, vz), (ax, ay, az)]

def tick(particles):
    return [update(particle) for particle in particles]

def is_divering(particle):
    i, position, velocity, acceleration = particle

    px, py, pz = position
    vx, vy, vz = velocity
    ax, ay, az = acceleration

    return vx * ax > 0 and vy * ay >= 0 and vz * az >= 0

def diverging(particles):
    return [particle for particle in particles if is_divering(particle)]

def simulate(particles, n=1000):
    nticks = 0

    for _ in range(n):
        particles = tick(particles)
        nticks += 1

    return particles

def dist(particle):
    i, position, velocity, acceleration = particle
    px, py, pz = position
    return abs(px) + abs(py) + abs(pz)

def closest(particles):
    return min(particles, key=lambda p: dist(p))

def main():
    with open('test_case.txt', 'r') as particles_input:
        particles = read(particles_input)
        assert (closest(simulate(particles, n=3))[0]) == 0

    with open('input.txt', 'r') as particles_input:
        particles = read(particles_input)
        print('Answer: ', closest(simulate(particles, n=1000))[0])




if __name__ == '__main__':
    main()
