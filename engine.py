class Engine:
    def __init__(self):
        self.is_running = False

    def start(self):
        self.is_running = True
        print("Engine started.")

    def stop(self):
        self.is_running = False
        print("Engine stopped.")


class FuelPump:
    def __init__(self, fuel_level=0):
        self.fuel_level = fuel_level

    def fill_tank(self, amount):
        self.fuel_level += amount
        print(f"Tank filled with {amount} liters of fuel.")

    def pump_fuel(self):
        if self.fuel_level > 0:
            self.fuel_level -= 1
            print("Fuel pumped.")
        else:
            print("Tank is empty.")


class IgnitionSystem:
    def __init__(self):
        self.is_on = False

    def ignite(self):
        self.is_on = True
        print("Ignition on.")

    def extinguish(self):
        self.is_on = False
        print("Ignition off.")


class AutomationProcess:
    def __init__(self):
        self.engine = Engine()
        self.fuel_pump = FuelPump()
        self.ignition_system = IgnitionSystem()

    def start_engine(self):
        self.fuel_pump.fill_tank(10)
        self.ignition_system.ignite()
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()
        self.ignition_system.extinguish()

    def run(self):
        self.start_engine()
        for i in range(10):
            self.fuel_pump.pump_fuel()
        self.stop_engine()
