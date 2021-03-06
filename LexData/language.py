"""
This module simply contains a few common Languages with their language-codes
and QIDs for easier use.
"""
from dataclasses import dataclass


@dataclass
class Language:
    """Dataclass representing a language"""

    short: str
    qid: str


en = Language("en", "Q1860")
de = Language("de", "Q188")
fr = Language("fr", "Q150")
# https://w.wiki/qeu
_aa = Language("aa", "Q27811")
_ab = Language("ab", "Q5111")
_af = Language("af", "Q14196")
_ak = Language("ak", "Q28026")
_am = Language("am", "Q28244")
_an = Language("an", "Q8765")
_ar = Language("ar", "Q13955")
_as = Language("as", "Q29401")
_av = Language("av", "Q29561")
_ay = Language("ay", "Q4627")
_az = Language("az", "Q9292")
_ba = Language("ba", "Q13389")
_be = Language("be", "Q9091")
_bg = Language("bg", "Q7918")
_bi = Language("bi", "Q35452")
_bm = Language("bm", "Q33243")
_bn = Language("bn", "Q9610")
_bo = Language("bo", "Q34271")
_br = Language("br", "Q12107")
_bs = Language("bs", "Q9303")
_ca = Language("ca", "Q7026")
_ce = Language("ce", "Q33350")
_ch = Language("ch", "Q33262")
_co = Language("co", "Q33111")
_cr = Language("cr", "Q33390")
_cs = Language("cs", "Q9056")
_cv = Language("cv", "Q33348")
_cy = Language("cy", "Q9309")
_da = Language("da", "Q9035")
_de = Language("de", "Q188")
_dv = Language("dv", "Q32656")
_dz = Language("dz", "Q33081")
_ee = Language("ee", "Q30005")
_el = Language("el", "Q9129")
_el = Language("el", "Q36510")
_en = Language("en", "Q1860")
_eo = Language("eo", "Q143")
_es = Language("es", "Q1321")
_et = Language("et", "Q9072")
_eu = Language("eu", "Q8752")
_fa = Language("fa", "Q9168")
_ff = Language("ff", "Q33454")
_fi = Language("fi", "Q1412")
_fj = Language("fj", "Q33295")
_fo = Language("fo", "Q25258")
_fr = Language("fr", "Q150")
_fy = Language("fy", "Q27175")
_ga = Language("ga", "Q9142")
_gd = Language("gd", "Q9314")
_gl = Language("gl", "Q9307")
_gn = Language("gn", "Q35876")
_gu = Language("gu", "Q5137")
_gv = Language("gv", "Q12175")
_ha = Language("ha", "Q56475")
_he = Language("he", "Q9288")
_hi = Language("hi", "Q1568")
_ho = Language("ho", "Q33617")
_hr = Language("hr", "Q6654")
_ht = Language("ht", "Q33491")
_hu = Language("hu", "Q9067")
_hy = Language("hy", "Q8785")
_hz = Language("hz", "Q33315")
_id = Language("id", "Q9240")
_ig = Language("ig", "Q33578")
_ii = Language("ii", "Q34235")
_ik = Language("ik", "Q27183")
_is = Language("is", "Q294")
_it = Language("it", "Q652")
_iu = Language("iu", "Q29921")
_ja = Language("ja", "Q5287")
_jv = Language("jv", "Q33549")
_ka = Language("ka", "Q8108")
_kg = Language("kg", "Q33702")
_ki = Language("ki", "Q33587")
_kj = Language("kj", "Q1405077")
_kk = Language("kk", "Q9252")
_kl = Language("kl", "Q25355")
_km = Language("km", "Q9205")
_kn = Language("kn", "Q33673")
_ko = Language("ko", "Q9176")
_kr = Language("kr", "Q36094")
_ks = Language("ks", "Q33552")
_ku = Language("ku", "Q36368")
_kv = Language("kv", "Q36126")
_kw = Language("kw", "Q25289")
_ky = Language("ky", "Q9255")
_lb = Language("lb", "Q9051")
_lg = Language("lg", "Q33368")
_li = Language("li", "Q102172")
_ln = Language("ln", "Q36217")
_lo = Language("lo", "Q9211")
_lt = Language("lt", "Q9083")
_lu = Language("lu", "Q36157")
_lv = Language("lv", "Q9078")
_mg = Language("mg", "Q7930")
_mh = Language("mh", "Q36280")
_mi = Language("mi", "Q36451")
_mk = Language("mk", "Q9296")
_ml = Language("ml", "Q36236")
_mn = Language("mn", "Q9246")
_mr = Language("mr", "Q1571")
_ms = Language("ms", "Q9237")
_mt = Language("mt", "Q9166")
_my = Language("my", "Q9228")
_na = Language("na", "Q13307")
_nb = Language("nb", "Q25167")
_nd = Language("nd", "Q35613")
_ne = Language("ne", "Q33823")
_ng = Language("ng", "Q33900")
_nl = Language("nl", "Q7411")
_nn = Language("nn", "Q25164")
_no = Language("no", "Q9043")
_nr = Language("nr", "Q36785")
_nv = Language("nv", "Q13310")
_ny = Language("ny", "Q33273")
_oc = Language("oc", "Q14185")
_oj = Language("oj", "Q33875")
_om = Language("om", "Q33864")
_or = Language("or", "Q33810")
_os = Language("os", "Q33968")
_pa = Language("pa", "Q58635")
_pl = Language("pl", "Q809")
_ps = Language("ps", "Q58680")
_pt = Language("pt", "Q5146")
_qu = Language("qu", "Q5218")
_rm = Language("rm", "Q13199")
_rn = Language("rn", "Q33583")
_ro = Language("ro", "Q7913")
_ru = Language("ru", "Q7737")
_rw = Language("rw", "Q33573")
_sc = Language("sc", "Q33976")
_sd = Language("sd", "Q33997")
_se = Language("se", "Q33947")
_sg = Language("sg", "Q33954")
_sh = Language("sh", "Q9301")
_si = Language("si", "Q13267")
_sk = Language("sk", "Q9058")
_sl = Language("sl", "Q9063")
_sm = Language("sm", "Q34011")
_sn = Language("sn", "Q34004")
_so = Language("so", "Q13275")
_sq = Language("sq", "Q8748")
_sr = Language("sr", "Q9299")
_ss = Language("ss", "Q34014")
_st = Language("st", "Q34340")
_su = Language("su", "Q34002")
_sv = Language("sv", "Q9027")
_sw = Language("sw", "Q7838")
_ta = Language("ta", "Q5885")
_te = Language("te", "Q8097")
_tg = Language("tg", "Q9260")
_th = Language("th", "Q9217")
_ti = Language("ti", "Q34124")
_tk = Language("tk", "Q9267")
_tl = Language("tl", "Q34057")
_tn = Language("tn", "Q34137")
_to = Language("to", "Q34094")
_tr = Language("tr", "Q256")
_ts = Language("ts", "Q34327")
_tt = Language("tt", "Q25285")
_tw = Language("tw", "Q36850")
_ty = Language("ty", "Q34128")
_ug = Language("ug", "Q13263")
_uk = Language("uk", "Q8798")
_ur = Language("ur", "Q1617")
_uz = Language("uz", "Q9264")
_ve = Language("ve", "Q32704")
_vi = Language("vi", "Q9199")
_wa = Language("wa", "Q34219")
_wo = Language("wo", "Q34257")
_xh = Language("xh", "Q13218")
_yi = Language("yi", "Q8641")
_yo = Language("yo", "Q34311")
_za = Language("za", "Q13216")
_zh = Language("zh", "Q7850")
_zu = Language("zu", "Q10179")
