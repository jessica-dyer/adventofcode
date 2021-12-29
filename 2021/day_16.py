from abc import ABC, abstractmethod

input = '38006F45291200'


def hex_to_binary(input: str):
    integer = int(input, 16)
    binary_value = str(bin(integer))[2:]
    missing_padding_count = len(binary_value) % 4
    binary_value = ('0' * missing_padding_count) + binary_value
    return binary_value


binary_input = hex_to_binary(input)


class AbstractPacket(ABC):
    def __init__(self, version, type, original_bit_length):
        self.version = version
        self.type = type
        self.original_bit_length = original_bit_length

    @abstractmethod
    def sum_of_version_and_all_sub_packet_versions(self):
        pass

class LiteralPacket(AbstractPacket):
    def __init__(self, version, literal_value, original_bit_length):
        super().__init__(version, 4, original_bit_length)
        self.literal_value = literal_value

    def sum_of_version_and_all_sub_packet_versions(self):
        return self.version  # LiteralPackets don't have sub-packets


class OperatorPacket(AbstractPacket):
    def __init__(self, version: int, type: int, array_of_subpackets: list, original_bit_length):
        super().__init__(version, type, original_bit_length)
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
        literal_value = 42  # should be 2021 for input D2FE28
        original_bit_length = 6  # should be 21 for input D2FE28
        final_binary = ''
        for index in range(0, len(remaining_binary_string), 5):
            current_five_char = remaining_binary_string[index:index + 5]
            if current_five_char[0] == '0':
                original_bit_length += len(current_five_char)
                final_binary += current_five_char[1:5]
                literal_value = binary_to_decimal(final_binary)
                break
            final_binary += current_five_char[1:5]
            original_bit_length += len(current_five_char)
        new_packet = LiteralPacket(version, literal_value, original_bit_length)
        return new_packet

    # return type is an instance of AbstractPacket
    def build_operator_packet(self, version, type, remaining_binary_string):
        sub_packets = []
        length_type_id = remaining_binary_string[0]
        remaining_binary_string = remaining_binary_string[1:len(remaining_binary_string)]
        original_bit_length = 42
        # TODO: build subpackets
        if length_type_id == '0':
            length_of_sub_packets = binary_to_decimal(remaining_binary_string[0:15])
        elif:
            length_of_sub_packets = binary_to_decimal(remaining_binary_string[0:11])
        new_packet = OperatorPacket(version, type, sub_packets, original_bit_length)
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


def get_length_of_sub_packets(binary_string: str):
    length_type_id = binary_string[6]
    if length_type_id == '0':
        bits = binary_string[7:22]
    else:
        bits = binary_string[7:18]
    dec = binary_to_decimal(bits)
    return dec


my_packet_factory = PacketFactory(binary_input)
print(my_packet_factory.get_sum_of_versions())
