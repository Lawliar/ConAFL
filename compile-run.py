import os
import sys
def main(argv):
  files = ''
  print(argv)
  for eachfile in argv:
    files += eachfile + ' '
  dirname = os.path.dirname(argv[0])
  thisDirname = os.path.dirname(os.path.realpath(__file__)) 
  sys.path.append(thisDirname)
  cmd = os.path.join(thisDirname,'afl-gcc')+ ' -pthread -g ' + files + '-o '+os.path.join(dirname,'executable')
  print(cmd)
  os.system(cmd)
  assert(os.path.exists(os.path.join(dirname,'conafl.txt')))#means compile success
  cmd = 'rm -f '+os.path.join(dirname,'conafl.txt')
  os.system(cmd)
  if os.path.exists(os.path.join(dirname,'out')):
    cmd = 'rm -rf '+os.path.join(dirname,'out')
    os.system(cmd)
    os.mkdir(os.path.join(dirname,'out'))
  if not os.path.exists(os.path.join(dirname,'in')):
    os.mkdir(os.path.join(dirname,'in'))
  cmd =os.path.join(thisDirname,'afl-fuzz')+ ' -m 1GB -i ' + os.path.join(dirname,'in') + ' -o' + os.path.join(dirname,'out') + ' -- ' + os.path.join(dirname,'executable') + ' @@'
  os.system(cmd)
if __name__ == '__main__':
  main(sys.argv[1:])
