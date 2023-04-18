import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n, m = 3, 4
infos = [['main', 'FolderA', 1],
['main', 'FolderB', 1],
['FolderA', 'File1', 0],
['FolderA', 'File2', 0],
['FolderB', 'FolderC', 1],
['FolderB', 'File1', 0],
['FolderB', 'File3', 0]]

q = 3
folders = ['main','main/FolderA','main/FolderB','main/FolderB/FolderC']

files = {}
parent_folder = {}
folder_in_files = [[] for _ in range(q)]
ans = [[0] * 2 for _ in range(q)]

# parent_folder에 각각 상위 폴더 적어두고,
# infos 돌리면서 상위 폴더의 상위 폴더가 있는지 재귀적으로 확인 총 결과 -> '/'로 붙이기 그래서 folders에 index 찾아서 파일 넣어두기,

for i in range(n+m):
    [p,f,c]= infos[i]
    if c == 1:
        parent_folder[f] = p

print(parent_folder)

def find_parent_folder(p,ans):
    parent_parent_folder = parent_folder.get(p)
    # print('ans',ans)
    if parent_parent_folder:
        return find_parent_folder(parent_parent_folder,parent_parent_folder+'/'+ans)
    return ans

for i in range(n+m):
    [p,f,c]= infos[i]
    folder = find_parent_folder(p,p)
    
    # print('1 full folder',folder)
    # print("c is ",c)
    if c == 1:
        folder += '/'+f
    print('folder',folder)
    # print('')
    if folder in folders:
        folder_index = folders.index(folder)
        if c == 0:
            folder_in_files[folder_index].append(f)

# print(folder_in_files)

for i in range(q):
    for j in range(i+1,q):
        if folders[i]+'/' in folders[j]:
            for f in folder_in_files[j]:
                folder_in_files[i].append(f)

for i in range(q):
    f = folder_in_files[i]
    ans[i] = [len(set(f)),len(f)]
# print(folder_in_files,ans)

for a in ans:
    print(a[0], a[1])