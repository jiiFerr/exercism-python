def proteins(input_strand):
    proteins_list = {
        'AUG': 'Methionine'
        , "UUU": "Phenylalanine"
        , "UUC": "Phenylalanine"
        , "UUA": "Leucine"
        , "UUG": "Leucine"
        , "UCU": "Serine"
        , "UCC": "Serine"
        , "UCA": "Serine"
        , "UCG": "Serine"
        , "UAU": "Tyrosine"
        , "UAC": "Tyrosine"
        , "UGU": "Cysteine"
        , "UGC": "Cysteine"
        , "UGG": "Tryptophan"
        , "UAA": "STOP"
        , "UAG": "STOP"
        , "UGA": "STOP"
    }

    return_list = []
    strand_list = [input_strand[i:i + 3] for i in range(0, len(input_strand), 3)]
    for strand in strand_list:
        if strand in proteins_list:
            if proteins_list[strand] is "STOP":
                break
            else:
                return_list.append(proteins_list[strand])

    return (return_list)
