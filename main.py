from rdkit import Chem
from rdkit.Chem import AllChem

# 输入分子的SMILES表示
smiles = "C1=CC2=C(C3=C(C=CC=N3)C=C2)N=C1"		# 替换为您的分子的SMILES表示

# 创建分子对象
mol = Chem.MolFromSmiles(smiles)

# 计算Morgan指纹
morgan_fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=64)

# 计算ECFP指纹
ecfp_fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=64)

# 将位串转换为字符串
morgan_bit_string = morgan_fp.ToBitString()
ecfp_bit_string = ecfp_fp.ToBitString()

print("Morgan指纹:", morgan_bit_string)
print("ECFP指纹:", ecfp_bit_string)