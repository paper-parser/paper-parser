""" Test PCE parcer """

import chemdataextractor as cde

from ...extracted_info import PCEParser

class TestPCEParser(BaseParser):

    def setUp(self):
        # Add PCE parcer to CDE paragraph parser object
        cde.doc.text.Paragraph.parsers.append(PCEParser())
        # Load in test document from paper
        # (https://onlinelibrary.wiley.com/doi/full/10.1002/anie.201406466)
        self.hard_test_txt = cde.doc.text.Document(
            cde.doc.text.Paragraph(u'Solar cells containing 1 display PCEs up to 4.73 %. Though devices containing 2 have exceeded PCEs of 15 %,2a–2c their moisture sensitivity remains a concern for large‐scale device fabrication or their long‐term use. The layered structure of 1 aids the formation of high‐quality films that show greater moisture resistance compared to 2. The larger bandgap of 1 also affords a higher VOC value of 1.18 V compared to devices with 2. Further improvements in material structure and device engineering, including making appropriate electronic contact with the anisotropic inorganic sheets, should increase the PCEs of these devices. In particular, higher values of n as single‐phase materials or as mixtures may allow for lower bandgaps and higher carrier mobility in the inorganic layers while the organic layers provide additional tunability. For example, hydrophobic fluorocarbons could increase moisture stability, conjugated organic layers could facilitate charge transport, and organic photosensitizers could improve the absorption properties of the material. We are focused on manipulating this extraordinarily versatile platform through synthetic design.'),
            cde.doc.text.Caption(u'PXRD patterns of films of (PEA)2(MA)2[Pb3I10] (1), (MA)[PbI3] formed from PbI2 (2 a), and (MA)[PbI3] formed from PbCl2 (2 b), which were exposed to 52 % relative humidity. Annealing of films of 2 a (15 minutes) and 2 b (80 minutes) was conducted at 100 °C prior to humidity exposure. Asterisks denote the major reflections from PbI2.')
            )
        self.easy_test_txt = cde.doc.text.Document(
            cde.doc.text.Paragraph(u'Solar cells containing H20 have a PCE of 6 %')
            )

    def test_interpret(self):
        find_pce_list = []
        for dictionary in self.easy_test_txt:
            find_pce_list.append('pce' in dictionary)
        assert (True in find_pce_list) == True, "PCE not found in easy test sentence"

        find_pce_list_hard = []
        for dictionary in self.hard_test_txt:
            find_pce_list_hard.append('pce' in dictionary)
        assert (True in find_pce_list_hard) == True, "PCE not found in hard test sentence"

        # Should find name and labels in the hard test text
        pce_dicts = self.hard_test_txt[find_pce_list_hard]
        for pce_dict in pce_dicts:
            assert 'names' in pce_dicts == True
            assert 'labels' in pce_dicts == True



