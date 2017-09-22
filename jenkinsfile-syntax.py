import sublime
import sublime_plugin


class JenkinsfileSyntax(sublime_plugin.EventListener):
    def on_load(self, view):
        file = view.file_name().split('/')

        filename = file[len(file) - 1]

        if filename.lower() == 'jenkinsfile':
            view.set_syntax_file('Packages/jenkinsfile-syntax/Groovy.tmLanguage')

