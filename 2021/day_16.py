from abc import ABC, abstractmethod

input = 'D2FE28'


def hex_to_binary(input: str):
    integer = int(input, 16)
    binary_value = str(bin(integer))[2:]
    missing_padding_count = len(binary_value) % 4
    binary_value = ('0' * missing_padding_count) + binary_value
    return binary_value


binary_input = hex_to_binary(input)


class AbstractPacket(ABC):
    def __init__(self, version, type):
        self.version = version
        self.type = type

    @abstractmethod
    def sum_of_version_and_all_sub_packet_versions(self):
        pass

class LiteralPacket(AbstractPacket):
    def __init__(self, version, literal_value):
        super().__init__(version, 4)
        self.literal_value = literal_value

    def sum_of_version_and_all_sub_packet_versions(self):
        return self.version  # LiteralPackets don't have sub-packets


class OperatorPacket(AbstractPacket):
    def __init__(self, version: int, type: int, array_of_subpackets: list):
        super().__init__(version, type)
        self.array_of_subpackets = array_of_subpackets

    def sum_of_version_and_all_sub_packet_versions(self):
        return self.version
#         TODO: Deal with sub-packets

class PacketFactory:
    def __init__(self, binary_string):
        self.root_packet = self.build_unknown_packet(binary_string)

    # return type is an instance of AbstractPacket
    def build_unknown_packet(self, remaining_binary_string):
        new_packet = None
        version = get_version(remaining_binary_string)
        type = get_type(remaining_binary_string)
        remaining_binary_string = remaining_binary_string[6:]
        if type == 4:
            new_packet = self.build_literal_packet(version, type, remaining_binary_string)
        else:
            new_packet = self.build_operator_packet(version, type, remaining_binary_string)
        return new_packet

    # return type is an instance of AbstractPacket
    def build_literal_packet(self, version, type, remaining_binary_string):
        literal_value = 42
        # TODO: come up with a literal value using remaining_binary_string
        new_packet = LiteralPacket(version, literal_value)
        return new_packet

    # return type is an instance of AbstractPacket
    def build_operator_packet(self, version, type, remaining_binary_string):
        sub_packets = []
        # TODO: build subpackets
        new_packet = OperatorPacket(version, type, sub_packets)
        return new_packet

    def get_sum_of_versions(self):
        sum = self.root_packet.sum_of_version_and_all_sub_packet_versions()
        return sum

# Takes: a string of binary


# Returns: a decimal representation of binary base 2 array
def binary_to_decimal(binary_string: str):
    base_2_array = []
    total = 0
    for i in range(len(binary_string)):
        current_base_2 = 2 ** i
        base_2_array.append(current_base_2)
    base_2_array.reverse()
    index: int
    for index in range(len(binary_string)):
        integer = int(binary_string[index])
        if integer == 1:
            total = total + base_2_array[index]
    return total


# Takes: binary string
# Returns: an integer that is the version number which is the first 3 bits of the binary string
def get_version(binary_string: str):
    current_string = binary_string[:3]
    decimal = binary_to_decimal(current_string)
    return decimal


def get_type(binary_string: str):
    current_string = binary_string[3:6]
    decimal = binary_to_decimal(current_string)
    return decimal


def get_literal_type_four(binary_string: str):
    string_length = len(binary_string)
    literal = binary_string[6:string_length]
    final_string = ''
    for index in range(0, len(literal), 5):
        current_five_char = literal[index:index + 5]
        if len(current_five_char) < 5:
            final_string = binary_to_decimal(final_string)
            return final_string
        final_string += current_five_char[1:5]


def get_length_of_sub_packets(binary_string: str):
    length_type_id = binary_string[6]
    if length_type_id == '0':
        bits = binary_string[7:22]
    else:
        bits = binary_string[7:18]
    dec = binary_to_decimal(bits)
    return dec


def run_decode(binary_string: str):
    current_version = get_version(binary_string)
    current_type = get_type(binary_string)

    if current_type == 4:
        return get_literal_type_four(binary_string)
    else:
        get_length_of_sub_packets(binary_string)


my_packet_factory = PacketFactory(binary_input)
print(my_packet_factory.get_sum_of_versions())
