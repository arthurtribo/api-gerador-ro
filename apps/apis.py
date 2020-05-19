import numpy
from flask import Blueprint, jsonify, Request
from dictionary import get_database
from apps.models import technicalReserve
from apps.models import insuranceIndicators
from apps.models import assets  
from apps.models import liabilities
from apps.models import resultDemonstration
from apps.models import administrativeExpense
from apps.models import financialExpense
from apps.models import taxExpense


bp = Blueprint('all', __name__)

filtro = {
    "technical_reserve": {
        "NIVEL": ["5","7","9"],
        "Conta": [
            "2.1.6",
            "2.1.6.1",
            "2.1.6.1.1",
            "2.1.6.1.5",
            "2.1.6.1.6",
            "2.1.6.1.7",
            "2.1.6.1.9",
            "2.1.6.2",
            "2.1.6.2.1",
            "2.1.6.2.5",
            "2.1.6.2.6",
            "2.1.6.2.7",
            "2.1.6.2.9",
            "1.1.9",
            "1.1.9.1",
            "1.1.9.1.1",
            "1.1.9.1.2",
            "1.1.9.3",
            "1.1.9.3.1",
            "1.1.9.3.2",
            "1.1.9.3.5",
            "1.1.9.3.6",
            "1.1.9.3.7",
            "1.2.1.1.2",
        ]
    },
    "insurance_indicators": {
        "NIVEL": ["5","7","9"],
        "Conta": [
            "3.1.1",
            "3.1.4",
            "3.1.1",
            "3.1.5",
            "3.1.1",
            "3.1.9.3",
            "3.1.1",
            "3.5",
            "3.1.1",
            "3.1.3",
            "3.1.4",
            "3.1.5",
            "3.1.9",
            "3.5",
            "3.1.1",
            "3.1.3",
            "3.1.4",
            "3.1.5",
            "3.1.9",
            "3.5",
            "3.6",
        ]
    },
    "Assets": {
        "NIVEL": ["5","7","9"],
        "Conta": [
            "1",
            "1.1",
            "1.1.1",
            "1.1.1.1",
            "1.1.1.3",
            "1.1.2",
            "1.1.2.6",
            "1.1.2.8",
            "1.1.3",
            "1.1.3.1",
            "1.1.3.4",
            "1.1.3.8",
            "1.1.4",
            "1.1.4.1",
            "1.1.4.2",
            "1.1.4.4",
            "1.1.4.5",
            "1.1.4.6",
            "1.1.4.8",
            "1.1.5",
            "1.1.5.1",
            "1.1.5.2",
            "1.1.7",
            "1.1.7.1",
            "1.1.7.2",
            "1.1.8",
            "1.1.8.1",
            "1.1.9",
            "1.1.9.1",
            "1.1.9.3",
            "1.2",
            "1.2.1",
            "1.2.1.1",
            "1.2.1.3",
            "1.2.2",
            "1.2.2.1",
            "1.2.2.3",
            "1.2.3",
            "1.2.3.1",
            "1.2.3.2",
            "1.2.3.3",
            "1.2.3.8",
        ]
    },
    "liabilities": {
        "NIVEL": ["1","3","5","7"],
        "Conta": [
            "2",
            "2.1",
            "2.1.1",
            "2.1.1.1",
            "2.1.1.2",
            "2.1.1.3",
            "2.1.1.6",
            "2.1.1.9",
            "2.1.2",
            "2.1.2.1",
            "2.1.2.3",
            "2.1.2.4",
            "2.1.2.5",
            "2.1.2.8",
            "2.1.6",
            "2.1.6.1",
            "2.1.6.2",
            "2.2",
            "2.2.8",
            "2.2.8.2",
            "2.2.8.4",
            "2.4",
            "2.4.1",
            "2.4.1.1",
            "2.4.1.4",
            "2.4.1.5",
            "2.4.1.6",
            "2.4.1.8",
            "2.4.1.9",
            "3",
        ]
    },
    "result_demonstration": {
        "NIVEL": ["1","3","5","7"],
        "Conta": [
            "3",
            "3.1",
            "3.1.1",
            "3.1.1.1",
            "3.1.1.8",
            "3.1.3",
            "3.1.3.1",
            "3.1.3.3",
            "3.1.3.4",
            "3.1.3.5",
            "3.1.3.6",
            "3.1.3.7",
            "3.1.4",
            "3.1.4.1",
            "3.1.4.5",
            "3.1.5",
            "3.1.5.1",
            "3.1.5.2",
            "3.1.9",
            "3.1.9.1",
            "3.1.9.3",
            "3.1.9.4",
            "3.5",
            "3.5.1",
            "3.5.1.1",
            "3.5.2",
            "3.5.2.1",
            "3.5.3",
            "3.5.3.1",
            "3.5.4",
            "3.5.4.1",
            "3.5.5",
            "3.5.5.1",
            "3.5.6",
            "3.5.6.1",
            "3.5.7",
            "3.5.7.1",
            "3.5.8",
            "3.5.8.1",
            "3.6",
            "3.6.1",
            "3.6.1.2",
            "3.6.1.3",
            "3.6.1.6",
            "3.6.1.9",
            "3.6.2",
            "3.6.2.1",
            "3.6.2.2",
            "3.6.2.3",
            "3.6.2.9",
            "3.7",
            "3.7.1",
            "3.7.1.1",
            "3.8",
            "3.8.1",
            "3.8.1.1",
            "3.9",
            "3.9.1",
            "3.9.1.1",
            "3.9.2",
            "3.9.2.1",
        ]
    },
    "administrative_expense": {
        "NIVEL": ["3","5","7","9"],
        "Conta": [
            "3.5",
            "3.5.1",
            "3.5.1.1",
            "3.5.1.1.1",
            "3.5.1.1.2",
            "3.5.1.1.3",
            "3.5.1.1.4",
            "3.5.1.1.5",
            "3.5.1.1.6",
            "3.5.1.1.7",
            "3.5.1.1.8",
            "3.5.2",
            "3.5.2.1",
            "3.5.2.1.1",
            "3.5.3",
            "3.5.3.1",
            "3.5.3.1.1",
            "3.5.3.1.2",
            "3.5.3.1.3",
            "3.5.3.1.4",
            "3.5.3.1.5",
            "3.5.3.1.6",
            "3.5.3.1.7",
            "3.5.3.1.8",
            "3.5.3.1.9",
            "3.5.4",
            "3.5.4.1",
            "3.5.4.1.1",
            "3.5.5",
            "3.5.5.1",
            "3.5.5.1.1",
            "3.5.5.1.2",
            "3.5.5.1.8",
            "3.5.6",
            "3.5.6.1",
            "3.5.6.1.1",
            "3.5.7",
            "3.5.7.1",
            "3.5.7.1.1",
            "3.5.8",
            "3.5.8.1",
            "3.5.8.1.1",
        ]
    },
    "financial_expense": {
        "NIVEL": ["3","5","7"],
        "Conta": [
            "3.6",
            "3.6.1",
            "3.6.1.2",
            "3.6.1.3",
            "3.6.1.6",
            "3.6.1.9",
            "3.6.2",
            "3.6.2.1",
            "3.6.2.2",
            "3.6.2.3",
            "3.6.2.9",
        ]
    },
    "tax_expense": {
        "NIVEL": ["3","5","7","9"],
        "Conta": [
            "3.9",
            "3.9.1",
            "3.9.1.1",
            "3.9.1.1.1",
            "3.9.2",
            "3.9.2.1",
            "3.9.2.1.1",
        ]
    },

}

def prepare_entry(description):
    return {
        "DESCRICAO": description,
        "janeiro": 0,
        "fevereiro": 0,
        "marco": 0,
        # "abril": 0,
        # "maio": 0,
        # "junho": 0,
        # "julho": 0,
        # "agosto": 0,
        # "setembro": 0,
        # "outubro": 0,
        # "novembro": 0,
        # "dezembro": 0
    }

def populate(complete_list, target_list, month):
    for record in complete_list:
        for target in target_list:
            if record["DESCRICAO"] == target["DESCRICAO"]:
                target[month] = record["SALDO ATUAL"]
                break

def filter_by_month_and_report(entries_raw, month, report):
    entries = entries_raw[month]
    entries = [e for e in entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    entries = [e for e in entries if e["CONTA"] in filtro[report]["Conta"]]
    return entries

@bp.route('/<string:report>/complete')
def complete(report):
    print(report)
    entries_db = get_database()
    entries = entries_db.values()

    entries = [e for elist in entries for e in elist]
    entries = [e for e in entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    entries = [e for e in entries if e["CONTA"] in filtro[report]["Conta"]]
    data_return = [prepare_entry(uniq_desc) for uniq_desc in sorted(numpy.unique([e["DESCRICAO"] for e in entries]))]

    populate(filter_by_month_and_report(entries_db, "janeiro", report), data_return, "janeiro")
    populate(filter_by_month_and_report(entries_db, "fevereiro", report), data_return, "fevereiro")
    populate(filter_by_month_and_report(entries_db, "marco", report), data_return, "marco")
    #populate(filter_by_month_and_report(entries_db, "abril", report), data_return, "abril")
    #populate(filter_by_month_and_report(entries_db, "maio", report), data_return, "maio")
    #populate(filter_by_month_and_report(entries_db, "junho", report), data_return, "junho")
    #populate(filter_by_month_and_report(entries_db, "julho", report), data_return, "julho")
    #populate(filter_by_month_and_report(entries_db, "agosto", report), data_return, "agosto")
    #populate(filter_by_month_and_report(entries_db, "setembro", report), data_return, "setembro")
    #populate(filter_by_month_and_report(entries_db, "outubro", report), data_return, "outubro")
    #populate(filter_by_month_and_report(entries_db, "novembro", report), data_return, "novembro")
    #populate(filter_by_month_and_report(entries_db, "dezembro", report), data_return, "dezembro")


    #populate(entries_fevereiro, data_return, "fevereiro")
    #populate(entries_marco, data_return, "marco")
    # populate(entries_abril, data_return, "abril")
    # populate(entries_maio, data_return, "maio")
    # populate(entries_junho, data_return, "junho")
    # populate(entries_julho, data_return, "julho")
    # populate(entries_agosto, data_return, "agosto")
    # populate(entries_setembro, data_return, "setembro")
    # populate(entries_outubro, data_return, "outubro")
    # populate(entries_novembro, data_return, "novembro")
    # populate(entries_dezembro, data_return, "dezembro")
    #sorted(data_return, key=locate_key)
    return jsonify(data_return)

@bp.route('/<string:report>/janeiro')
def read_reportjan(report):

    jan_entries = get_database()["janeiro"]
    jan_entries = [e for e in jan_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    jan_entries = [e for e in jan_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(jan_entries);

@bp.route('/<string:report>/fevereiro')
def read_reportfev(report):
  
    fev_entries = get_database()["fevereiro"]
    fev_entries = [e for e in fev_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    fev_entries = [e for e in fev_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(fev_entries)

@bp.route('/<string:report>/marco')
def read_reportmar(report):
        
    mar_entries = get_database()["marco"]
    mar_entries = [e for e in mar_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    mar_entries = [e for e in mar_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(mar_entries)

@bp.route('/<string:report>/abril')
def read_reportabr(report):
        
    abr_entries = get_database()["abril"]
    abr_entries = [e for e in abr_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    abr_entries = [e for e in abr_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(abr_entries)

@bp.route('/<string:report>/maio')
def read_reportmai(report):
        
    mai_entries = get_database()["maio"]
    mai_entries = [e for e in mai_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    mai_entries = [e for e in mai_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(mai_entries)

@bp.route('/<string:report>/junho')
def read_reportjun(report):

    jun_entries = get_database()["junho"]    
    jun_entries = [e for e in jun_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    jun_entries = [e for e in jun_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(jun_entries)

@bp.route('/<string:report>/julho')
def read_reportjul(report):
        
    jul_entries = get_database()["julho"]
    jul_entries = [e for e in jul_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    jul_entries = [e for e in jul_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(jul_entries)

@bp.route('/<string:report>/agosto')
def read_reportago(report):

    ago_entries = get_database()["agosto"]    
    ago_entries = [e for e in ago_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    ago_entries = [e for e in ago_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(ago_entries)
        
@bp.route('/<string:report>/setembro')
def read_reportset(report):

    set_entries = get_database()["setembro"]
    set_entries = [e for e in set_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    set_entries = [e for e in set_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(set_entries)
        
@bp.route('/<string:report>/outubro')
def read_reportout(report):

    out_entries = get_database()["outubro"]
    out_entries = [e for e in out_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    out_entries = [e for e in out_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(out_entries)
        
@bp.route('/<string:report>/novembro')
def read_reportnov(report):

    nov_entries = get_database()["novembro"]
    nov_entries = [e for e in nov_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    nov_entries = [e for e in nov_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(nov_entries)
        
@bp.route('/<string:report>/dezembro')
def read_reportdez(report):

    dez_entries = get_database()["dezembro"]
    dez_entries = [e for e in dez_entries if e["NIVEL"] in filtro[report]["NIVEL"]]
    dez_entries = [e for e in dez_entries if e["CONTA"] in filtro[report]["Conta"]]
    return jsonify(dez_entries)







