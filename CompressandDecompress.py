import zlib, base64


def compress(input, output):
    # Open the file and read whats in it
    readData = open(input, 'r').read()

    # Convert string to bytes to enable compression
    convert_toBytes = bytes(readData, 'utf-8')

    # Use the zlib and base64 libraries to encode and compress file
    compress_data = base64.b64encode(zlib.compress(convert_toBytes, 9))

    # Decode the file from bytes back to string
    decode_file = compress_data.decode('utf-8')

    # write this to a new file
    compressed_file = open(output, 'w')
    compressed_file.write(decode_file)


def decompress(input_file, output_file):
    # open the input file and read it
    new_file = open(input_file, 'r').read()
    # perform encoding to enable compression
    encode_file = new_file.encode('utf-8')
    # decompress and decode input file
    decompressed_data = zlib.decompress(base64.b64decode(encode_file))
    # decode file from bytes back to string
    decoded_data = decompressed_data.decode('utf-8')

    # open a new file and write the new decoded data into it
    decoded_file = open(output_file, 'w')
    decoded_file.write(decoded_data)


