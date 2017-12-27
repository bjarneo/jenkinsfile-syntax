import sublime
import sublime_plugin


class JenkinsfileSyntax(sublime_plugin.EventListener):
    def on_load(self, view):
        filename = view.file_name().split('/')

        if len(filename) and 'jenkinsfile' in filename[-1].lower():
            view.set_syntax_file('Packages/jenkinsfile-syntax/Groovy.tmLanguage')

