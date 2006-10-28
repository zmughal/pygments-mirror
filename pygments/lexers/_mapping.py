# -*- coding: utf-8 -*-
"""
    pygments.lexers._mapping
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer mapping defintions. This file is generated by itself. Everytime
    you change something on a builtin lexer defintion, run this script from
    the lexers folder to update it.

    Do not alter the LEXERS dictionary by hand.

    :copyright: 2006 by Armin Ronacher, Georg Brandl.
    :license: GNU LGPL, see LICENSE for more details.
"""

LEXERS = {
    'BooLexer': ('pygments.lexers.dotnet', 'Boo', ('boo',), ('*.boo',)),
    'BrainfuckLexer': ('pygments.lexers.other', 'Brainfuck', ('brainfuck', 'bf'), ('*.bf', '*.b')),
    'CLexer': ('pygments.lexers.compiled', 'C', ('c',), ('*.c', '*.h')),
    'CSharpLexer': ('pygments.lexers.dotnet', 'C#', ('csharp', 'c#'), ('*.cs',)),
    'CppLexer': ('pygments.lexers.compiled', 'C++', ('cpp', 'c++'), ('*.cpp', '*.hpp', '*.c++', '*.h++')),
    'CssDjangoLexer': ('pygments.lexers.templates', 'CSS+Django', ('css+django',), ()),
    'CssErbLexer': ('pygments.lexers.templates', 'CSS+Ruby', ('css+erb', 'css+ruby'), ()),
    'CssGenshiLexer': ('pygments.lexers.templates', 'CSS+Genshi Text', ('css+genshitext', 'css+genshi'), ()),
    'CssLexer': ('pygments.lexers.web', 'CSS', ('css',), ('*.css',)),
    'CssPhpLexer': ('pygments.lexers.templates', 'CSS+PHP', ('css+php',), ()),
    'CssSmartyLexer': ('pygments.lexers.templates', 'CSS+Smarty', ('css+smarty',), ()),
    'DelphiLexer': ('pygments.lexers.compiled', 'Delphi', ('delphi', 'pas', 'pascal', 'objectpascal'), ('*.pas',)),
    'DiffLexer': ('pygments.lexers.text', 'Diff', ('diff',), ('*.diff', '*.patch')),
    'DjangoLexer': ('pygments.lexers.templates', 'django template', ('django',), ()),
    'ErbLexer': ('pygments.lexers.templates', 'ERB', ('erb',), ()),
    'GenshiLexer': ('pygments.lexers.templates', 'Genshi', ('genshi', 'kid', 'xml+genshi', 'xml+kid'), ('*.kid',)),
    'GenshiTextLexer': ('pygments.lexers.templates', 'Genshi Text', ('genshitext',), ()),
    'HtmlDjangoLexer': ('pygments.lexers.templates', 'HTML+Django', ('html+django',), ()),
    'HtmlGenshiLexer': ('pygments.lexers.templates', 'HTML+Genshi', ('html+genshi', 'html+kid'), ()),
    'HtmlLexer': ('pygments.lexers.web', 'HTML', ('html',), ('*.html', '*.htm', '*.xhtml')),
    'HtmlPhpLexer': ('pygments.lexers.templates', 'HTML+PHP', ('html+php',), ('*.phtml',)),
    'HtmlSmartyLexer': ('pygments.lexers.templates', 'HTML+Smarty', ('html+smarty',), ()),
    'IniLexer': ('pygments.lexers.text', 'INI', ('ini', 'cfg'), ('*.ini', '*.cfg')),
    'IrcLogsLexer': ('pygments.lexers.text', 'IRC logs', ('irc',), ()),
    'JavaLexer': ('pygments.lexers.compiled', 'Java', ('java',), ('*.java',)),
    'JavascriptDjangoLexer': ('pygments.lexers.templates', 'JavaScript+Django', ('js+django', 'javascript+django'), ()),
    'JavascriptErbLexer': ('pygments.lexers.templates', 'JavaScript+Ruby', ('js+erb', 'javascript+erb', 'js+ruby', 'javascript+ruby'), ()),
    'JavascriptGenshiLexer': ('pygments.lexers.templates', 'JavaScript+Genshi Text', ('js+genshitext', 'js+genshi', 'javascript+genshitext', 'javascript+genshi'), ()),
    'JavascriptLexer': ('pygments.lexers.web', 'JavaScript', ('js', 'javascript'), ('*.js',)),
    'JavascriptPhpLexer': ('pygments.lexers.templates', 'JavaScript+PHP', ('js+php', 'javascript+php'), ()),
    'JavascriptSmartyLexer': ('pygments.lexers.templates', 'JavaScript+Smarty', ('js+smarty', 'javascript+smarty'), ()),
    'LuaLexer': ('pygments.lexers.agile', 'Lua', ('lua',), ('*.lua',)),
    'MakefileLexer': ('pygments.lexers.text', 'Makefile', ('make', 'makefile', 'mf'), ('*.mak', 'Makefile', 'makefile')),
    'PerlLexer': ('pygments.lexers.agile', 'Perl', ('perl', 'pl'), ('*.pl', '*.pm')),
    'PhpLexer': ('pygments.lexers.web', 'PHP', ('php', 'php3', 'php4', 'php5'), ('*.php', '*.php[345]')),
    'PythonConsoleLexer': ('pygments.lexers.agile', 'Python console session', ('pycon',), ()),
    'PythonLexer': ('pygments.lexers.agile', 'Python', ('python', 'py'), ('*.py', '*.pyw')),
    'RawTokenLexer': ('pygments.lexers.special', 'Raw token data', ('raw',), ('*.raw',)),
    'RhtmlLexer': ('pygments.lexers.templates', 'RHTML', ('rhtml', 'html+erb', 'html+ruby'), ('*.rhtml',)),
    'RubyConsoleLexer': ('pygments.lexers.agile', 'Ruby irb session', ('rbcon', 'irb'), ()),
    'RubyLexer': ('pygments.lexers.agile', 'Ruby', ('rb', 'ruby'), ('*.rb', '*.rbw', 'Rakefile', '*.rake', '*.gemspec', '*.rbx')),
    'SmartyLexer': ('pygments.lexers.templates', 'Smarty', ('smarty',), ()),
    'SqlLexer': ('pygments.lexers.other', 'SQL', ('sql',), ('*.sql',)),
    'TexLexer': ('pygments.lexers.text', 'TeX', ('tex', 'latex'), ('*.tex', '*.aux', '*.toc')),
    'TextLexer': ('pygments.lexers.special', 'Text only', ('text',), ('*.txt',)),
    'VbNetLexer': ('pygments.lexers.dotnet', 'VB.net', ('vb.net', 'vbnet'), ('*.vb', '*.bas')),
    'XmlDjangoLexer': ('pygments.lexers.templates', 'XML+Django', ('xml+django',), ()),
    'XmlErbLexer': ('pygments.lexers.templates', 'XML+Ruby', ('xml+erb', 'xml+ruby'), ()),
    'XmlLexer': ('pygments.lexers.web', 'XML', ('xml',), ('*.xml',)),
    'XmlPhpLexer': ('pygments.lexers.templates', 'XML+PHP', ('xml+php',), ()),
    'XmlSmartyLexer': ('pygments.lexers.templates', 'XML+Smarty', ('xml+smarty',), ())
}

if __name__ == '__main__':
    import sys
    import os

    # lookup lexers
    found_lexers = []
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
    for filename in os.listdir('.'):
        if filename.endswith('.py') and not filename.startswith('_'):
            module_name = 'pygments.lexers.%s' % filename[:-3]
            print module_name
            module = __import__(module_name, None, None, [''])
            for lexer_name in module.__all__:
                lexer = getattr(module, lexer_name)
                found_lexers.append(
                    '%r: %r' % (lexer_name,
                                (module_name,
                                 lexer.name,
                                 tuple(lexer.aliases),
                                 tuple(lexer.filenames))))
    # sort them, that should make the diff files for svn smaller
    found_lexers.sort()

    # extract useful sourcecode from this file
    f = file(__file__)
    try:
        content = f.read()
    finally:
        f.close()
    header = content[:content.find('LEXERS = {')]
    footer = content[content.find("if __name__ == '__main__':"):]

    # write new file
    f = file(__file__, 'w')
    f.write(header)
    f.write('LEXERS = {\n    %s\n}\n\n' % ',\n    '.join(found_lexers))
    f.write(footer)
    f.close()
