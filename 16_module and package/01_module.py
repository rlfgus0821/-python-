# import sys
#
# module_name = sys.builtin_module_names
# print(module_name)
# ('_abc', '_ast', '_bisect', '_blake2', '_codecs',
#  '_codecs_cn', '_codecs_hk', '_codecs_iso2022',
#  '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections',
#  '_contextvars', '_csv', '_datetime', '_functools', '_heapq',
#  '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec',
#  '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha2', '_sha3',
#  '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable',
#  '_thread', '_tokenize', '_tracemalloc', '_typing', '_warnings', '_weakref',
#  '_winapi', '_xxinterpchannels', '_xxsubinterpreters', 'array', 'atexit',
#  'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc',
#  'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time',
#  'winreg', 'xxsubtype', 'zlib')

# 모듈 불러오기 ->  import 모듈명 -> 모듈명.메소드명
import caculator
print(caculator.add(10, 3))

from showinfo import showphone, showname
showname()
showphone()

# as
# 모듈 별칭 지정
import showinfo as si
si.showname()
si.showphone()
# 함수 별칭 지정
from showinfo import showphone as sp
sp()
showphone()

