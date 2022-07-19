def split_f(file_link: str):
    chunk_size = 1024 * 100  # Bytes, 100kb
    chunk = 0
    array_of_chunks = []

    with open(file_link, 'rb') as file_main:
        byte = file_main.read(chunk_size)

        while byte:
            with open(''.join(file_main.name.split('.')[:-1]) + '_chunk_' + str(chunk)+'.txt', 'wb') as file_chunk:
                file_chunk.write(byte)
            chunk += 1
            byte = file_main.read(chunk_size)
            array_of_chunks.append(str(file_chunk.name))

        chunks = " ".join(array_of_chunks)  # Convert array to string

    return(
        {
            'chunks': chunks,
            'name': file_main.name
        })


def merge_f(file_info : dict):
    array_of_chunks = file_info.get('chunks').split()  # Convert string to array
    with open('copy_'+file_info.get('name'), 'wb') as return_file:

        for chunk in array_of_chunks:
            with open(chunk, 'rb') as chunk:
                return_file.write(chunk.read())

    print('Файл')

