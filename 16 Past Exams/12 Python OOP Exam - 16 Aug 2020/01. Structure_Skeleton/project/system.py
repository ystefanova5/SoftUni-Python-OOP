from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):
        if hardware_name not in [x.name for x in System._hardware]:
            return "Hardware does not exist"

        hardware = [x for x in System._hardware if x.name == hardware_name][0]
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        if hardware_name not in [x.name for x in System._hardware]:
            return "Hardware does not exist"

        hardware = [x for x in System._hardware if x.name == hardware_name][0]
        software = LightSoftware(name, capacity_consumption, memory_consumption)

        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        if hardware_name not in [x.name for x in System._hardware] or \
                software_name not in [x.name for x in System._software]:
            return "Some of the components do not exist"

        hardware = [x for x in System._hardware if x.name == hardware_name][0]
        software = [x for x in System._software if x.name == software_name][0]

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory_consumption = sum(x.memory_consumption for x in System._software)
        total_memory_on_hardware = sum(x.memory for x in System._hardware)
        total_capacity_consumption = sum(x.capacity_consumption for x in System._software)
        total_capacity_on_hardware = sum(x.capacity for x in System._hardware)

        result = [
            "System Analysis",
            f"Hardware Components: {len(System._hardware)}",
            f"Software Components: {len(System._software)}",
            f"Total Operational Memory: {total_memory_consumption} / {total_memory_on_hardware}",
            f"Total Capacity Taken: {total_capacity_consumption} / {total_capacity_on_hardware}"
        ]

        return '\n'.join(result)

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            result.append(f"Hardware Component - {hardware.name}")

            express_software = [x for x in hardware.software_components if x.software_type == "Express"]
            light_software = [x for x in hardware.software_components if x.software_type == "Light"]

            software_components = "None"
            if hardware.software_components:
                software_components = ', '.join(x.name for x in hardware.software_components)

            result.append(f"Express Software Components: {len(express_software)}")
            result.append(f"Light Software Components: {len(light_software)}")
            result.append(f"Memory Usage: {hardware.memory_usage} / {hardware.memory}")
            result.append(f"Capacity Usage: {hardware.capacity_usage} / {hardware.capacity}")
            result.append(f"Type: {hardware.hardware_type}")
            result.append(f"Software Components: {software_components}")

        return '\n'.join(result)
