#!/usr/bin/env python
# encoding: utf-8
"""
Python bindings of webrtc audio processing
"""

import sys
from glob import glob
try:
    from setuptools import setup, Extension
    from distutils.command.build import build
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
    from distutils.command.build import build
    from distutils.command.install import install

PY2 = sys.version_info[0] == 2


include_dirs = ['src', 'webrtc-audio-processing']

libraries = ['pthread', 'stdc++']

define_macros = [
    ('WEBRTC_LINUX', None),
    ('WEBRTC_POSIX', None),
    ('WEBRTC_NS_FLOAT', None),
    ('WEBRTC_AUDIO_PROCESSING_ONLY_BUILD', None)
]

extra_compile_args = ['-std=c++11']

ap_sources = []
ap_dir_prefix = 'webrtc-audio-processing/webrtc/'
for i in xrange(8):
    ap_sources += glob(ap_dir_prefix + '*.c*')
    ap_dir_prefix += '*/'

ap_sources = [src for src in ap_sources if src.find('mips.') < 0 and src.find('neon.') < 0]
ap_sources = [src for src in ap_sources if src.find('win.') < 0 and src.find('condition_variable.') < 0 and src.find('rw_lock_generic.') < 0]

sources = (
    ap_sources +
    ['src/audio_processing_module.cpp', 'src/webrtc_audio_processing.i']
)

swig_opts = (
    ['-c++'] +
    ['-I' + h for h in include_dirs]
)


setup(
    name='webrtc_audio_processing',
    version='0.0.1',
    description='Python bindings of webrtc audio processing',
    long_description=__doc__,
    author='Yihui Xiong',
    author_email='yihui.xiong@hotmail.com',
    maintainer='Yihui Xiong',
    maintainer_email='yihui.xiong@hotmail.com',
    url='https://github.com/xiongyihui/python-webrtc-audio-processing',
    download_url='https://pypi.python.org/pypi/webrtc_audio_processing',
    packages=['webrtc_audio_processing'],
    ext_modules=[
        Extension(
            name='webrtc_audio_processing._webrtc_audio_processing',
            sources=sources,
            swig_opts=swig_opts,
            include_dirs=include_dirs,
            libraries=libraries,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args
        )
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: C++'
    ],
    license='BSD',
    keywords=['webrtc audioprocessing', 'voice activity detection', 'noise suppression', 'automatic gain control'],
    platforms=['Linux'],
    package_dir={
        'webrtc_audio_processing': 'src'
    }
)