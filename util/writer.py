def side_by_side(s1, s2, space = " "):
	'''
	Writes two string left-right of eachother, with the given space between each two rows
	'''

	text = ""

	split1 = str(s1).split("\n")
	ind1 = 0
	split2 = str(s2).split("\n")
	ind2 = 0

	len1 = max(map(len, split1))
	len2 = max(map(len, split2))

	first = True

	while ind1 < len(split1) or ind2 < len(split2):
		if not first:
			text += "\n"
		else:
			first = False
		text += "{:<{}}".format(split1[ind1] if ind1 < len(split1) else "", len1)
		text += space
		text += "{:<{}}".format(split2[ind2] if ind2 < len(split2) else "", len2)

		ind1 += 1
		ind2 += 1

	return text