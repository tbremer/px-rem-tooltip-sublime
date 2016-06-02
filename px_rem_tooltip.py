import re
import sublime, sublime_plugin

class PXRem(sublime_plugin.EventListener):
	def on_selection_modified(self, view):
		if (view.is_popup_visible()) is True:
			view.hide_popup();

		syntax = view.settings().get('syntax')

		SYNTAX_SEARCH = '(?:s|l)?(?:a|c|e)ss'
		VALID_INPUT_SEARCH = '[\d.]+(?:px|rem)'
		PX_SEARCH = 'px'
		DIGIT_SEARCH = '([\d.]+)'

		popup_numbers = []

		if re.search(SYNTAX_SEARCH, syntax, re.IGNORECASE) is None:
			return

		cur_line_text = view.substr(view.line(view.sel()[0]))
		matches = re.findall(VALID_INPUT_SEARCH, cur_line_text)

		if len(matches) == 0:
			return

		for match in matches:
			type_match = re.search(PX_SEARCH, match, re.IGNORECASE)

			if type_match:
				inner_match = re.search(DIGIT_SEARCH, match)
				number = float(inner_match.group()) / 16
				string = str(number) + 'rem;'
			else:
				inner_match = re.search(DIGIT_SEARCH, match)
				number = float(inner_match.group()) * 16
				string = str(number) + 'px;'

			popup_numbers.append(string)

		popup_string = ' '.join(popup_numbers)

		view.show_popup(popup_string)
