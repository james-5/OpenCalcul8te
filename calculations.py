import math

def calculate_elastic_collision(m1, m2, v1, v2):
    if m1 + m2 == 0:
        raise ZeroDivisionError("Total mass cannot be zero.")
    v1_new = (m1 - m2) / (m1 + m2) * v1 + (2 * m2) / (m1 + m2) * v2
    v2_new = (m2 - m1) / (m1 + m2) * v2 + (2 * m1) / (m1 + m2) * v1
    return v1_new, v2_new

def calculate_momentum(m, v):
    return m * v

def calculate_parallax(p):
    if p == 0:
        raise ZeroDivisionError("Parallax angle cannot be zero.")
    return 1.0 / p

def calculate_ohms_law(v, i, r):
    filled = sum(1 for x in (v, i, r) if x != '')
    if filled < 2:
        raise ValueError("At least two values (V, I, or R) must be provided.")
    v = float(v) if v else None
    i = float(i) if i else None
    r = float(r) if r else None
    if v is not None and i is not None:
        r = v / i if i != 0 else float('inf')
    elif v is not None and r is not None:
        i = v / r if r != 0 else float('inf')
    elif i is not None and r is not None:
        v = i * r
    return v or 0, i or 0, r or 0

def calculate_power(v, i, r):
    filled = sum(1 for x in (v, i, r) if x != '')
    if filled < 2:
        raise ValueError("At least two values (V, I, or R) must be provided.")
    v = float(v) if v else None
    i = float(i) if i else None
    r = float(r) if r else None
    if v is not None and i is not None:
        return v * i
    elif i is not None and r is not None:
        return i * i * r
    elif v is not None and r is not None:
        return (v * v) / r
    return 0

def calculate_resistors_series(r1, r2):
    return r1 + r2

def calculate_resistors_parallel(r1, r2):
    if r1 == 0 or r2 == 0:
        raise ValueError("Resistances cannot be zero.")
    return (r1 * r2) / (r1 + r2)

def calculate_gauss_law_e(q, a):
    EPSILON_0 = 8.85e-12
    if a == 0:
        raise ValueError("Area cannot be zero.")
    return q / (EPSILON_0 * a)

def calculate_gauss_law_b(flux):
    return "Zero (no magnetic monopoles)" if flux == 0 else "Non-zero flux detected"

def calculate_faraday_law(dphi_b, dt):
    if dt == 0:
        raise ValueError("Time difference cannot be zero.")
    return -dphi_b / dt

def calculate_ampere_law(i, dphi_e, dt, l):
    MU_0 = 4 * math.pi * 1e-7
    EPSILON_0 = 8.85e-12
    if l == 0:
        raise ValueError("Length cannot be zero.")
    displacement_current = EPSILON_0 * (dphi_e / dt) if dt != 0 else 0
    return (MU_0 * (i + displacement_current)) / l

def calculate_ph(h):
    if h <= 0:
        raise ValueError("Hydrogen ion concentration must be positive.")
    return -math.log10(h)

def calculate_lhopital_rule(f_str, g_str, x):
    try:
        # Simple symbolic differentiation (basic example)
        def derivative(expr):
            if 'x' not in expr:
                return 0
            if expr == 'x':
                return 1
            if expr.startswith('x^'):
                power = float(expr[2:])
                return power * (x ** (power - 1))
            return 0  # Placeholder for more complex expressions
        f_deriv = derivative(f_str)
        g_deriv = derivative(g_str)
        if g_deriv == 0:
            raise ValueError("Denominator derivative is zero.")
        return f_deriv / g_deriv
    except Exception:
        raise ValueError("Invalid function format or undefined limit.")

def calculate_derivative(f_str, x):
    try:
        # Simple numerical derivative approximation
        h = 1e-5
        def eval_f(expr, x_val):
            if expr == 'x':
                return x_val
            if expr.startswith('x^'):
                power = float(expr[2:])
                return x_val ** power
            return float(expr) if expr.replace('.', '').isdigit() else 0
        f_x = eval_f(f_str, x)
        f_xh = eval_f(f_str, x + h)
        return (f_xh - f_x) / h
    except Exception:
        raise ValueError("Invalid function format.")

def calculate_integral(f_str, a, b):
    try:
        # Simple numerical integration (trapezoidal rule with 100 points)
        n = 100
        dx = (b - a) / n
        result = 0
        for i in range(n):
            x0 = a + i * dx
            x1 = a + (i + 1) * dx
            def eval_f(expr, x_val):
                if expr == 'x':
                    return x_val
                if expr.startswith('x^'):
                    power = float(expr[2:])
                    return x_val ** power
                return float(expr) if expr.replace('.', '').isdigit() else 0
            y0 = eval_f(f_str, x0)
            y1 = eval_f(f_str, x1)
            result += (y0 + y1) * dx / 2
        return result
    except Exception:
        raise ValueError("Invalid function format or integration limits.")

def calculate_lagrangian_eulerian(x0, t):
    # Simple example: v(x,t) = 1 m/s, x(t) = x0 + v*t
    v = 1.0  # Constant velocity for Eulerian field
    x_lagrangian = x0 + v * t
    return x_lagrangian, v

def calculate_lagrangian_trajectory(x0, v0, t):
    return x0 + v0 * t

def calculate_boyles_law(p1, v1, v2):
    if v1 == 0 or v2 == 0:
        raise ValueError("Volumes cannot be zero.")
    return (p1 * v1) / v2

def calculate_ideal_gas_law(p, v, n, t):
    R = 0.0821  # L·atm/(mol·K)
    if n == 0 or t == 0:
        raise ValueError("Moles and temperature must be positive.")
    return (p * v) / (n * t)

def calculate_isentropic_flow(t1, p1, p2):
    GAMMA = 1.4
    if p1 == 0 or p2 == 0:
        raise ValueError("Pressures cannot be zero.")
    return t1 * (p2 / p1) ** ((GAMMA - 1) / GAMMA)

def calculate_poiseuille_law(r, delta_p, eta, l):
    if eta == 0 or l == 0:
        raise ValueError("Viscosity and length cannot be zero.")
    return math.pi * r ** 4 * delta_p / (8 * eta * l)

def calculate_venturi_principle(a1, a2, v1):
    if a1 == 0 or a2 == 0:
        raise ValueError("Areas cannot be zero.")
    return (a1 * v1) / a2

def calculate_supersonic_flow(mach, p0, t0):
    GAMMA = 1.4
    if mach <= 0:
        raise ValueError("Mach number must be positive.")
    p_ratio = 1 / ((1 + (GAMMA - 1) / 2 * mach ** 2) ** (GAMMA / (GAMMA - 1)))
    t_ratio = 1 / (1 + (GAMMA - 1) / 2 * mach ** 2)
    rho_ratio = p_ratio / t_ratio
    return p_ratio * p0, t_ratio * t0, rho_ratio

def calculate_compressible_flow(p0, t0, a):
    GAMMA = 1.4
    R = 287  # J/(kg·K) for air
    if t0 == 0 or a == 0:
        raise ValueError("Temperature and area cannot be zero.")
    a_critical = math.sqrt(GAMMA * R * t0)  # Speed of sound
    mdot = p0 * a * a_critical / math.sqrt(R * t0) * math.sqrt((2 / (GAMMA - 1)) * ((2 / (GAMMA + 1)) ** ((GAMMA + 1) / (GAMMA - 1))))
    return mdot

def calculate_heat_capacity_ratio(cp, cv):
    if cv == 0:
        raise ValueError("Specific heat at constant volume cannot be zero.")
    return cp / cv

def calculate_isentropic_nozzle_flow(mach):
    GAMMA = 1.4
    if mach <= 0:
        raise ValueError("Mach number must be positive.")
    if mach == 1:
        return 1.0
    term = (GAMMA + 1) / (GAMMA - 1)
    return (1 / mach) * ((1 + (GAMMA - 1) / 2 * mach ** 2) ** (term / 2))