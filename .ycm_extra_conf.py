def Settings( **kwargs ):
  return {
    'flags': [ '-x', 'c++', '-Wall', '-Wextra', '-Werror', '-std=c++20',
                '-I/usr/local/lib/gcc/x86_64-pc-linux-gnu/14.1.0/../../../../include/c++/14.1.0',
                '-I/usr/local/lib/gcc/x86_64-pc-linux-gnu/14.1.0/../../../../include/c++/14.1.0/x86_64-pc-linux-gnu',
                '-I/usr/local/lib/gcc/x86_64-pc-linux-gnu/14.1.0/../../../../include/c++/14.1.0/backward',
                '-I/usr/local/lib/gcc/x86_64-pc-linux-gnu/14.1.0/include',
                '-I/usr/local/include',
                '-I/usr/local/lib/gcc/x86_64-pc-linux-gnu/14.1.0/include-fixed',
                '-I/usr/include',
              ],
  }
