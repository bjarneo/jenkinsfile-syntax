import sublime
import sublime_plugin


class JenkinsfileSyntax(sublime_plugin.EventListener):
    def on_load(self, view):
        filename = view.file_name().split('/')

        if filename[-1].lower() == 'jenkinsfile':
            view.set_syntax_file('Packages/jenkinsfile-syntax/Groovy.tmLanguage')

