""" Test PCE parcer """

import chemdataextractor as cde

from ..extracted_info import PCEParser

class TestPceParser(BaseParser):

    def setUp(self):
        # Add PCE parcer to CDE paragraph parser object
        cde.doc.text.Paragraph.parsers = [PCEParser()]

        # Load some test text
        self.easy_test_txt = cde.doc.text.Document(
            cde.doc.text.Paragraph(u'Solar cells containing H20 have a PCE of 6 %')
            )

        # Load in test document from paper
        # https://onlinelibrary.wiley.com/doi/full/10.1002/anie.201406466
        self.hard_test_txt = cde.doc.text.Document(
            cde.doc.text.Paragraph(u'Solar cells containing 1 display PCEs up to 4.73 %. Though devices containing 2 have exceeded PCEs of 15 %,2a–2c their moisture sensitivity remains a concern for large‐scale device fabrication or their long‐term use. The layered structure of 1 aids the formation of high‐quality films that show greater moisture resistance compared to 2. The larger bandgap of 1 also affords a higher VOC value of 1.18 V compared to devices with 2. Further improvements in material structure and device engineering, including making appropriate electronic contact with the anisotropic inorganic sheets, should increase the PCEs of these devices. In particular, higher values of n as single‐phase materials or as mixtures may allow for lower bandgaps and higher carrier mobility in the inorganic layers while the organic layers provide additional tunability. For example, hydrophobic fluorocarbons could increase moisture stability, conjugated organic layers could facilitate charge transport, and organic photosensitizers could improve the absorption properties of the material. We are focused on manipulating this extraordinarily versatile platform through synthetic design.'),
            cde.doc.text.Caption(u'PXRD patterns of films of (PEA)2(MA)2[Pb3I10] (1), (MA)[PbI3] formed from PbI2 (2 a), and (MA)[PbI3] formed from PbCl2 (2 b), which were exposed to 52 % relative humidity. Annealing of films of 2 a (15 minutes) and 2 b (80 minutes) was conducted at 100 °C prior to humidity exposure. Asterisks denote the major reflections from PbI2.')
            )

        # Second to last paragraph from
        # https://www.nature.com/articles/nmat4014
        # with only one PCE value reported
        self.second_to_last_para_w_1_pce_html = cde.doc.text.Document(
            cde.doc.text.Paragraph(u'To further enhance the performance of our cells fabricated by solvent engineering, we repeated the fabrication procedure using mp-TiO<sub>2</sub> with a thickness of <span class="stix"><span class="stix">∼</span></span>200 nm. The <i>J</i>–<i>V</i> curves and incident photon-to-current efficiency (IPCE) spectrum of the best performing solar cell are presented in <a href="https://www.nature.com/articles/nmat4014#f5" data-track="click" data-track-action="figure anchor" data-track-label="link">Fig.&nbsp;5</a>. The average values from the <i>J</i>–<i>V</i> curves from the reverse and forward scans (<a href="https://www.nature.com/articles/nmat4014#f5" data-track="click" data-track-action="figure anchor" data-track-label="link">Fig.&nbsp;5a</a>) exhibited a <i>J</i><sub>sc</sub> of 19.58 mA cm<sup>−2</sup>, <i>V</i><sub>oc</sub> of 1.105 V, and FF of 76.2%, corresponding to a PCE of 16.5% under standard AM 1.5 G conditions. The best device also showed a very broad IPCE plateau of over 80% between 420 and 700 nm, as shown in <a href="https://www.nature.com/articles/nmat4014#f5" data-track="click" data-track-action="figure anchor" data-track-label="link">Fig.&nbsp;5b</a>. The <i>J</i><sub>sc</sub> value integrated from the IPCE agreed well with that measured by <i>I</i>–<i>V</i>. In <a href="https://www.nature.com/articles/nmat4014#f5" data-track="click" data-track-action="figure anchor" data-track-label="link">Fig.&nbsp;5c</a> a histogram of the average PCEs for all of the independently fabricated cells contributing to our study is presented. Around 80% of the cells made using our process exhibited an overall efficiency exceeding of 15% under 1 sun conditions, proving the conceptual validity of a balanced thickness between the TiO<sub>2</sub> and thin upper layers. In addition, an evaluation of the available results allows us to conclude that this solvent-engineering approach provides a simple and effective means for realizing high-efficiency and low-cost perovskite-based solar cells. One of these devices was certified by the standardized method in a photovoltaics calibration laboratory, confirming a PCE of 16.2% under AM 1.5 G full sun')
                )
        # And conclution from same paper, which as 'PCE' after the value.
        self.conclusion_w_1_pce_html = cde.doc.text.Document(
            cde.doc.text.Paragraph(u'In summary, we developed a solvent-engineering technology for the deposition of extremely uniform perovskite layers, and demonstrated a solution-processed perovskite solar cell with 16.5% PCE under standard conditions (AM 1.5 G radiation, 100 mW cm<sup>−2</sup>). We proposed a plausible mechanism for the formation of uniform and dense perovskite layers during the solvent-engineering process. The formation of a stable MAI(Br)–PbI<sub>2</sub>–DMSO phase via an intercalation process during the dropwise application of a non-dissolving solvent was a decisive factor in retarding the rapid reaction between MAI(Br) and PbI(Br)<sub>2</sub>, which enabled the formation of a highly uniform and dense surface. Furthermore, we found that thick perovskite cells fabricated without mp-TiO<sub>2</sub> showed a large hysteresis and distortion between reverse and forward scans, and raised arguments about the estimation of conversion efficiencies for perovskite cells. Hence, the ratio of the thicknesses of the perovskite-infiltrated mp-TiO<sub>2</sub> and the pure perovskite should be optimized to fabricate efficient perovskite cells with coincident reverse and forward scans. These results will provide an effective strategy for forming uniform PbI<sub>2</sub>-based perovskite layers through intercalation, and lead to more efficient and cost-effective inorganic–organic hybrid heterojunction solar cells in the&nbsp;future.</p></div></div></section><section aria-labelledby="methods"><div class="serif article-section js-article-section cleared clear" id="methods-section"><h2 class="js-section-title section-title position-relative strong tighten-line-height background-gray-light pt20 pb6 pl0 pr20 standard-space-below mq640-pt20 mq640-pb10 mq640-pl20 mq640-mt0 mq640-ml-20 mq640-mr-20 extend-left small-space-above" id="methods"><span>Methods</span><span class="js-section-title-label block position-relative text18 text-blue pr20 icon-rotate icon-arrow-down-12x7-gray hide">Methods</span></h2><div class="pl20 mq875-pl0 js-collapsible-section" id="methods-content"><h3 class="h3 strong mb4">Solar cell fabrication.</h3><p>A dense blocking layer of TiO<sub>2</sub> (bl-TiO<sub>2</sub>, <span class="stix"><span class="stix">∼</span></span>70 nm in thickness) was deposited onto a F-doped SnO<sub>2</sub> (FTO, Pilkington, TEC8) substrate by spray pyrolysis, using a 20 mM titanium diisopropoxide bis(acetylacetonate) solution (Aldrich) at 450 °C to prevent direct contact between the FTO and the hole-conducting layer. A 200–300-nm-thick mesoporous TiO<sub>2</sub> (particle size: about 50 nm, crystalline phase: anatase) film was spin-coated onto the bl-TiO<sub>2</sub>/FTO substrate using home-made pastes<sup><a id="ref-link-section-38" title="Malinkiewicz, O. et al. Perovskite solar cells employing organic charge-transport layers. Nature Photon. 6, 128–132 ')
                )

    def test_interpret(self):
        # Mark each dictionary in list of dictionaries as True of False
        # depending on whether or not it contains the key 'pce'
        find_pce_list = []
        for dictionary in self.easy_test_txt:
            find_pce_list.append('pce' in dictionary)
        assert (True in find_pce_list) == True, "PCE not found in easy test sentence"

        # Same test on harder text with two PCE values
        find_pce_list_hard = []
        for dictionary in self.hard_test_txt:
            find_pce_list_hard.append('pce' in dictionary)
        assert (True in find_pce_list_hard) == True, "PCE not found in hard test sentence"

        # Test whether or not PCE values are associated with a
        # chemical name or label. Should find name and labels in the
        # hard test text.
        pce_dicts = self.hard_test_txt[find_pce_list_hard]
        for pce_dict in pce_dicts:
            assert 'names' in pce_dicts == True
            assert 'labels' in pce_dicts == True

        ## STILL IN DEVELOPMENT
        # # Test the text from https://www.nature.com/articles/nmat4014
        # find_in_nat_list
        # nat_sec_last_dicts = self.second_to_last_para_w_1_pce_html[find_pce_list_hard]
        # for pce_dict in pce_dicts:


