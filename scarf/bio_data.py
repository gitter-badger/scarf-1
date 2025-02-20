from typing import List

__all__ = ['s_phase_genes', 'g2m_phase_genes', 'datasets']

s_phase_genes: List[str] = [
    'MCM5', 'PCNA', 'TYMS', 'FEN1', 'MCM2', 'MCM4', 'RRM1', 'UNG', 'GINS2', 'MCM6',
    'CDCA7', 'DTL', 'PRIM1', 'UHRF1', 'MLF1IP', 'HELLS', 'RFC2', 'RPA2', 'NASP',
    'RAD51AP1', 'GMNN', 'WDR76', 'SLBP', 'CCNE2', 'UBR7', 'POLD3', 'MSH2', 'ATAD2',
    'RAD51', 'RRM2', 'CDC45', 'CDC6', 'EXO1', 'TIPIN', 'DSCC1', 'BLM', 'CASP8AP2',
    'USP1', 'CLSPN', 'POLA1', 'CHAF1B', 'BRIP1', 'E2F8'
]

g2m_phase_genes: List[str] = [
    'HMGB2', 'CDK1', 'NUSAP1', 'UBE2C', 'BIRC5', 'TPX2', 'TOP2A', 'NDC80', 'CKS2',
    'NUF2', 'CKS1B', 'MKI67', 'TMPO', 'CENPF', 'TACC3', 'FAM64A', 'SMC4', 'CCNB2',
    'CKAP2L', 'CKAP2', 'AURKB', 'BUB1', 'KIF11', 'ANP32E', 'TUBB4B', 'GTSE1',
    'KIF20B', 'HJURP', 'CDCA3', 'HN1', 'CDC20', 'TTK', 'CDC25C', 'KIF2C',
    'RANGAP1', 'NCAPD2', 'DLGAP5', 'CDCA2', 'CDCA8', 'ECT2', 'KIF23', 'HMMR',
    'AURKA', 'PSRC1', 'ANLN', 'LBR', 'CKAP5', 'CENPE', 'CTCF', 'NEK2', 'G2E3',
    'GAS2L3', 'CBX5', 'CENPA'
]

datasets = {
    'tenx_10k_pbmc_citeseq': [
        {'name': 'data.h5',
         'url': 'http://cf.10xgenomics.com/samples/cell-exp/3.0.0/pbmc_10k_protein_v3/'
                 'pbmc_10k_protein_v3_filtered_feature_bc_matrix.h5'}
    ],
    'tenx_1M_brain_rnaseq': [
        {'name': 'data.h5',
         'url': 'http://cf.10xgenomics.com/samples/cell-exp/1.3.0/1M_neurons/'
                '1M_neurons_filtered_gene_bc_matrices_h5.h5'}
    ],
    'zheng_68k_pbmc-fresh_rnaseq': [
        {'name': 'matrix.mtx.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '6089608fa9746602312f7347'},
        {'name': 'features.tsv.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '60896084a9746602372f77dd'},
        {'name': 'barcodes.tsv.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '60896085f1616002479cd02a'},
    ],
    'kang_ctrl_pbmc_rnaseq': [
        {'name': 'matrix.mtx.gz',
         'url': 'https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM2560nnn/GSM2560248/suppl/'
                'GSM2560248_2.1.mtx.gz'},
        {'name': 'features.tsv.gz',
         'url': 'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96583/suppl/'
                'GSE96583_batch2.genes.tsv.gz'},
        {'name': 'barcodes.tsv.gz',
         'url': 'https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM2560nnn/GSM2560248/suppl/'
                'GSM2560248_barcodes.tsv.gz'},
    ],
    'kang_stim_pbmc_rnaseq': [
        {'name': 'matrix.mtx.gz',
         'url': 'https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM2560nnn/GSM2560249/suppl/'
                'GSM2560249_2.2.mtx.gz'},
        {'name': 'features.tsv.gz',
         'url': 'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE96nnn/GSE96583/suppl/'
                'GSE96583_batch2.genes.tsv.gz'},
        {'name': 'barcodes.tsv.gz',
         'url': 'https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM2560nnn/GSM2560249/suppl/'
                'GSM2560249_barcodes.tsv.gz'},
    ],
    'tenx_10k_pbmc_atacseq': [
        {'name': 'data.h5',
         'url': 'http://cf.10xgenomics.com/samples/cell-atac/1.2.0/atac_pbmc_10k_nextgem'
                '/atac_pbmc_10k_nextgem_filtered_peak_bc_matrix.h5'}
    ],
    'bastidas_day15_pancreas_rnaseq': [
        {'name': 'data.h5ad',
         'url': 'https://github.com/theislab/scvelo_notebooks/raw/master/data/Pancreas/'
                'endocrinogenesis_day15.h5ad'}
    ],
    'baron_8k_pancreas_rnaseq': [
        {'name': 'matrix.mtx.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1d3386541a041414a914'},
        {'name': 'features.tsv.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1d3286541a041514b220'},
        {'name': 'barcodes.tsv.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1d32e80d370429a57906'},
    ],
    'muraro_2k_pancreas_rnaseq': [
        {'name': 'matrix.mtx.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1d86e80d37042ea589df'},
        {'name': 'features.tsv.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1d85ba0109040989135e'},
        {'name': 'barcodes.tsv.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1d84ba0109040d8931bb'},
    ],
    'segerstolpe_2k_pancreas_rnaseq': [
        {'name': 'matrix.mtx.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1d9e86541a040e14b481'},
        {'name': 'features.tsv.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1d9d86541a041514b340'},
        {'name': 'barcodes.tsv.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1d9de80d37042ea58a03'},
    ],
    'xin_1k_pancreas_rnaseq': [
        {'name': 'matrix.mtx.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1dd5ba010904098913a7'},
        {'name': 'features.tsv.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1dd4ba0109040c892074'},
        {'name': 'barcodes.tsv.gz',
         'url': 'https://files.de-1.osf.io/v1/resources/zeupv/providers/osfstorage/'
                '5ffe1dd4e80d37042aa56f5a'},
    ],
}
