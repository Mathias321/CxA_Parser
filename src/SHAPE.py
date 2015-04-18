from CadstarArcObj import *
import SHAPE
import PT
import CWSEMI
import ACWSEMI
import CWARC
import ACWARC

    # (FIGURE FIG30 LC5 NO_SHEET
    #     (OUTLINE (PT 50609500 26670000) (PT 50736500 26670000) (PT 50736500 26924000) (PT 50609500 26924000) (PT 50609500 26670000))
    # )
    #
    # (FIGURE FIG9 LC5 NO_SHEET
    #     (OPENSHAPE (PT 50038000 26416000) (PT 51308000 26416000))
    # )
    #
    # (FIGURE FIG2 LC5 NO_SHEET
    #     (OPENSHAPE (PT 51663600 25844500)
    #         (CWSEMI (PT 51663600 25971500))
    #         (CWSEMI (PT 51663600 25844500))
    #     )
    # )
    # (FIGURE FIG5 LC5 NO_SHEET
    #     (SOLID (PT 50673000 25882600)
    #         (CWSEMI (PT 50673000 25933400))
    #         (CWSEMI (PT 50673000 25882600))
    #     )
    # )



class SHAPE(CadstarArcObj):
    CAO_keyword = ""
    DICT_POSATTR = []
    DICT_ATTR = {}
    DICT_COLLECTION = {PT.PT : "points",
                       CWSEMI.CWSEMI : "cwsemi",
                       ACWSEMI.ACWSEMI : "acwsemi",
                       CWARC.CWARC : "cwarc",
                       ACWARC.ACWARC : "acwarc"}


class SOLID(SHAPE):
    CAO_keyword = "SOLID"


class OUTLINE(SHAPE):
    CAO_keyword = "OUTLINE"


class OPENSHAPE(SHAPE):
    CAO_keyword = "OPENSHAPE"


CadstarArcObj.register_sub_class(SOLID)
CadstarArcObj.register_sub_class(OUTLINE)
CadstarArcObj.register_sub_class(OPENSHAPE)