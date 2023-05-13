# Original demos
original1 = '''
Review: straining to get by on humor that is not even as daring as john ritter 's glory days on three 's company . 
label: negative
Review: , serves as a paper skeleton for some very good acting , dialogue , comedy , direction and especially charm . 
label: positive
Review: a whole lot of fun and funny in the middle , though somewhat less hard-hitting at the start and finish . 
label: positive
Review: might have been saved if the director , tom dey , had spliced together bits and pieces of midnight run and 48 hours ( and , for that matter , shrek ) 
label: negative
'''


# Flipping labels
flipping1 = '''Review: straining to get by on humor that is not even as daring as john ritter 's glory days on three 's company . 
label: positive
Review: , serves as a paper skeleton for some very good acting , dialogue , comedy , direction and especially charm . 
label: negative
Review: a whole lot of fun and funny in the middle , though somewhat less hard-hitting at the start and finish . 
label: negative
Review: might have been saved if the director , tom dey , had spliced together bits and pieces of midnight run and 48 hours ( and , for that matter , shrek ) 
label: positive
'''


# Input perturbation
perturbation1 = '''Review: Relying on humor that is reminiscent of John Ritter's glory days on Three's Company. 
label: negative
Review: serves as a paper framework for some standard acting, dialogue, comedy, direction, and charm. 
label: positive
Review: Generally average and neutral in the middle, albeit slightly less impactful at the start and finish.
label: positive
Review: The movie may have been different if the director, Tom Dey, had incorporated elements from Midnight Run and 48 Hours (and, incidentally, Shrek).
label: negative
'''


# Complementray explanation
complementary1 = '''Review: straining to get by on humor that is not even as daring as john ritter 's glory days on three 's company . 
Explanation: "straining to get by" and "not even as daring" indicate that the humor being discussed is seen as barely adequate and less bold compared to a past standard (John Ritter's glory days)
label: negative
Review: , serves as a paper skeleton for some very good acting , dialogue , comedy , direction and especially charm . 
Explanation: "very good acting", "dialogue", "comedy", "direction", and "especially charm" are generally associated with positive sentiments in the context of a review.
label: positive
Review: a whole lot of fun and funny in the middle , though somewhat less hard-hitting at the start and finish . 
Explanation: it describes the subject as "a whole lot of fun" and "funny", which are positive attributes. Although it mentions less positive aspects at the start and finish, the overall sentiment leans towards a positive experience.
label: positive
Review: might have been saved if the director , tom dey , had spliced together bits and pieces of midnight run and 48 hours ( and , for that matter , shrek ) 
explanation: it implies that the director's work was unsatisfactory and the film could have been better if it had incorporated elements from other successful films, suggesting that the film as it stands is not good enough.
label: negative
'''