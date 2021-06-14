import os
import string
import sys

from avro import schema
from avro import io
from avro import datafile

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.exit('Usage: %s <data_file>' % sys.argv[0])
  avro_file = sys.argv[1]
  writer = open(avro_file, 'wb')
  datum_writer = io.DatumWriter()
  
  # 코드 안에 에이브로 스키마 내장
  schema_object = schema.parse("""\
{ "type": "record",
  "name": "StringPair",
  "doc": "A pair of strings.",
  "fields": [
    {"name": "left", "type": "string"},
    {"name": "right", "type": "string"}
  ]
}""")

  dfw = datafile.DataFileWriter(writer, datum_writer, schema_object)

  # 표준 입력에서 여러 줄을 입력, ctrl+d 또는 ctrl+z 로 입력 종료
  lines = sys.stdin.readlines()
  for line in lines:
    (left, right) = line.strip().split(',')
    dfw.append({'left':left, 'right':right})
  dfw.close()