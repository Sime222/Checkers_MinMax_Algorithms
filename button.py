class Button():
	"""
	This class is used to create a button with a given image, position, text, font, base color and hovering color.
	It also has methods to update the button, check for input and change the color of the button.
	"""

	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		"""
		This is the constructor for the Button class. It takes in the following parameters:
		image: The image to be used for the button.
		pos: The position of the button.
		text_input: The text to be displayed on the button.
		font: The font to be used for the text.
		base_color: The base color of the button.
		hovering_color: The color of the button when it is being hovered over.
		"""
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		"""
		This method updates the button on the given screen.
		"""
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		"""
		This method checks if the given position is within the bounds of the button.
		It returns True if it is, False otherwise.
		"""
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		"""
		This method changes the color of the button based on the given position.
		If the position is within the bounds of the button, the color is changed to the hovering color.
		Otherwise, the color is changed to the base color.
		"""
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)