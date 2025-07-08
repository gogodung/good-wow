# -*- coding: utf-8 -*-
import streamlit as st

# RNA codon to amino acid mapping (64개 완전 버전)
codon_table = {
    'UUU': 'Phe', 'UUC': 'Phe',
    'UUA': 'Leu', 'UUG': 'Leu',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
    'AUG': 'Met',  # Start codon
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'UAU': 'Tyr', 'UAC': 'Tyr',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',
    'CAU': 'His', 'CAC': 'His',
    'CAA': 'Gln', 'CAG': 'Gln',
    'AAU': 'Asn', 'AAC': 'Asn',
    'AAA': 'Lys', 'AAG': 'Lys',
    'GAU': 'Asp', 'GAC': 'Asp',
    'GAA': 'Glu', 'GAG': 'Glu',
    'UGU': 'Cys', 'UGC': 'Cys',
    'UGG': 'Trp',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AGU': 'Ser', 'AGC': 'Ser',
    'AGA': 'Arg', 'AGG': 'Arg',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
}

# Streamlit 인터페이스
st.title("🧬 RNA → 아미노산 번역기")
st.markdown("DNA 또는 RNA 염기서열을 입력하면 **개시코돈(AUG)**부터 아미노산 서열로 번역합니다.")

user_input = st.text_input("🔡 염기서열 입력 (예: AUGGCCAUG...)", "").strip().upper()

if user_input:
    seq = user_input.replace(" ", "")
    if set(seq) <= {'A', 'T', 'C', 'G'}:
        st.info("DNA로 인식: RNA로 변환 중...")
        seq = seq.replace('T', 'U')

    start = seq.find("AUG")
    if start == -1:
        st.error("⚠️ 개시코돈(AUG)을 찾을 수 없습니다.")
    else:
        result = []
        for i in range(start, len(seq), 3):
            codon = seq[i:i+3]
            if len(codon) < 3:
                st.warning(f"⚠️ 불완전 코돈 무시됨: {codon}")
                break
            amino = codon_table.get(codon, '???')
            if amino == 'Stop':
                break
            result.append(amino)
        
        st.success("✅ 아미노산 서열:")
        st.markdown(" - ".join(result))
