from chemdataextractor.doc import Paragraph
import order

def test_syn_order():
    '''Tests if function syn_order works'''
    
    paragraph = Paragraph(
        'After drying, the HTM was deposited by spin-coating a solution of spiro-MeOTAD, 4-tert-butylpyridine, \
        lithium bis(trifluoromethylsulphonyl)imide and tris(2-(1H-pyrazol-1-yl)-4-tert-butylpyridine)cobalt(iii) \
        bis(trifluoromethylsulphonyl)imide in chlorobenzene.\
        Annealing the as-deposited films at 100\u2009°C for 45\u2009min in the N2-filled glove box \
        before spin-coating the hole transporter enabled full crystallization of the perovskite, darkening \
        the colour and resulting in an apparent growth of the crystal features visible in the SEM image, \
        as shown in Extended Data Fig. 1.')
    vb_order, vb_dict = order.syn_order(paragraph)
    
    assert vb_order[0][0] == 'dry', 'First action identified is incorrect'
    assert vb_order[0][1] == 0, 'Sentence number where first action is identified is incorrect'
    assert vb_order[3][0] == 'anneal', 'Fails to identify capitalized word'
    assert ['anneal', 'spin-coat'] in vb_dict.values(), \
    'Fails to store all steps found in vb_dict output'