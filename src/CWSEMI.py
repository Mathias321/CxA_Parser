from CadstarArcObj import *

    # (FIGURE FIG2 LC5 NO_SHEET
    #     (OPENSHAPE (PT 51663600 25844500)
    #         (CWSEMI (PT 51663600 25971500))
    #         (CWSEMI (PT 51663600 25844500))
    #     )
    # )

class CWSEMI(CadstarArcObj):
    CAO_keyword = "CWSEMI"


CadstarArcObj.register_sub_class(CWSEMI)