import csv


def read_file(filepath):
    read_file_info = getReadFilePath(filepath)
    csvreader = csv.reader(read_file_info)
    return csvreader


def getReadFilePath(read_file_path):
    fread = open(read_file_path, 'r')
    return fread


def getWriteFilePath(write_file_path):
    fwrite = open(write_file_path, 'w')
    return fwrite
