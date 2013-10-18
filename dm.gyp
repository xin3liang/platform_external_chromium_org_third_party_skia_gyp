# GYP for "dm" (Diamond Master, a.k.a Dungeon master, a.k.a GM 2).
# vim: set expandtab tabstop=4 shiftwidth=4
{
    'includes': [ 'apptype_console.gypi' ],

    'targets': [{
        'target_name': 'dm',
        'type': 'executable',
        'include_dirs': [
            '../dm',
            '../gm',
            '../src/core',
            '../src/effects',
            '../src/utils',
            '../src/utils/debugger',
        ],
        'includes': [ 'gmslides.gypi' ],
        'sources': [
            '../dm/DM.cpp',
            '../dm/DMComparisonTask.cpp',
            '../dm/DMCpuTask.cpp',
            '../dm/DMGpuTask.cpp',
            '../dm/DMReplayTask.cpp',
            '../dm/DMReporter.cpp',
            '../dm/DMTask.cpp',
            '../dm/DMTaskRunner.cpp',
            '../dm/DMUtil.cpp',
            '../dm/DMWriteTask.cpp',
            '../gm/gm.cpp',
            '../gm/gm_expectations.cpp',

            # TODO: split these out as a library in src/utils/debugger.
            '../src/utils/debugger/SkDebugCanvas.cpp',
            '../src/utils/debugger/SkDrawCommand.cpp',
            '../src/utils/debugger/SkObjectParser.cpp',
        ],
        'dependencies': [
            'skia_lib.gyp:skia_lib',
            'flags.gyp:flags',
            'jsoncpp.gyp:jsoncpp',
            'gputest.gyp:skgputest',
        ],
    }]
}
