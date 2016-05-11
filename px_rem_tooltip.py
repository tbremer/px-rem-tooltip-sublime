import re
import sublime, sublime_plugin

class PXRem(sublime_plugin.EventListener):
	def on_selection_modified(self, view):
		syntax = view.settings().get('syntax')

		popup_numbers = []

		if re.search('(?:s|l)?(?:a|c|e)ss', syntax, re.IGNORECASE) is None:
			return

		cur_line_text = view.substr(view.line(view.sel()[0]))

		for match in re.findall('\d+(?:px|rem)', cur_line_text):
			type_match = re.search('px', match)

			print(match)

			if type_match:
				inner_match = re.search('(\d+)', match)
				number = int(float(inner_match.group())) / 16
				string = str(number) + 'rem;'
			else:
				inner_match = re.search('(\d+)', match)
				number = int(float(inner_match.group())) * 16
				string = str(number) + 'px;'

			popup_numbers.append(string)

		popup_string = ' '.join(popup_numbers)

		view.show_popup(popup_string)
