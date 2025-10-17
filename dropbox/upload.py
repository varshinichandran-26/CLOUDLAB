import os
import dropbox
ACCESS_TOKEN = "sl.u.AGCbGzx92LBorDlFyTYtJgacBC0uNAXvYQZ1XK6c4U_LvKfYcYL1xlf2gtkCgxL4TRy4NP9t_eOw0PFl8MHmgePoj7PgNXZ-30HuFsY_MdW_BOzRhYfaKqGz9FhZ1IEL74CqNksoBbczSjYYqS7K16hIXqETGM2w-W9xk8FgaFywwE5fRdd9LCGvwi1G36pJIXEbbNq2Zk7XB_bqFav37JnMZ17QiSjTOUiYaqHA81XJo_q1TpeQa41v7PcPlRl9w0uovK4h0tNQJfzPFo8Ipc3muoC4SUMbMiuuANq8C3Y660heyTHKauH8Tnh9M01aFFaJksl2ORAqsvmM9MfEqkreowTCpR6v4NUZ1h5EBkXBBXXUsi70zmMtYyy8GWXNTBILADF8Kxus3z3at9aQYjoIVeCRl0PT-55jgOTVqGrYwhMko8vFc5QtRfzw9Pc_k_dNrSyzNe4qTBkhDgtUITRomNoVx5x7lbNmNQkT8YuZB3vTtfx-h1dhJfrUpzqadXLFUICtKQLWaJu5T2SyLmjav12nmYtcUbMZnsIaMXkumhELcu3XgesJR1Hp6r3FXVTn1shhWBI9-ooHLVg38yRzye9f0ZRMlfAEJPTLnPkLLi5lXBMxZTpMpWfjG5uAGKr26A6JtcjpQZYMbykzplmj2Kvz81UFrDHmCVJAYi6LOWu9u-gZAAz6OHW8k9ReIvSOpJBrUEaEzfQrJCe8dQIi-BLzC5IxnR_y_Jmww8xS0RPVFmEToekYbk_sQ2YZ-N5yRKi_1oALU5Iphjpox1yiJqBKkyPFnNn7mjAOhy8hEa41n8FhJNJZ-MZixThP-Cv2zrt5hxgzPoQF-BWdfPseEeHGcETejhPvIZ5pL9_2U3v0mE9VJRcYoA5nDSiHXPz3U-XSUEr_bcakEX3l_R2WvroaFhg-NFilq8vCieTVQxrJqneAxuUf4u8mXLPMUs-DVPBvzW4CFBFUTXa20Z_3h23S_Vdvyc4ZJ4mTD8m0cOYnFp85PGd0w_pNAntGQEDMQEAZdZEuj9YOFdllQ4LHqHEXlJkJ-qO-SdeY745Qmv212CDcjOzW5a-d_SXzZkIDsni3p85VyGVo3RYrWNquiOldkIJmIG4mo_rxASgZJ9TGhRs4imYRSGad27_FxjWlzMWNp6zVg3ARdj0Qq6qhweV0fehmOTXRCcAkljahXAHEabcQ05zpZ-dBhuRv5Q8qspLkszdRt4_g2ZB3C9SqLgS9GUBoY1KOtPu_iMY9IfXEMQO9WONeesuBF4P7_pOR-nSnsi7Y0pAQpM7IHcjWh88UKnzn7AQQ6oW03zcVijZ_xYDRrFXNL5VFOPCa5_q3esLnDUpgfTMLSykBI-EDj9S0OVSksti_AnOsJU9XheDxXpAyye7mo3KPRTUHGXIJlDUk_s_uQp0veySFRIlRpCnZWs50_tWXWuTLadd1xQ"
LOCAL_DIR = "diary_entries"   # where Flask saves files
DROPBOX_DIR = "/new-app"     # folder in Dropbox

dbx = dropbox.Dropbox(ACCESS_TOKEN)

def upload_file(local_path, dropbox_path):
    with open(local_path, "rb") as f:
        dbx.files_upload(
            f.read(), dropbox_path,
            mode=dropbox.files.WriteMode("overwrite")
        )
    print ("connected to dropbox sucessfully")
    print(f"✅ Uploaded {local_path} → {dropbox_path}")

def sync_folder(local_dir, dropbox_dir):
    for fname in os.listdir(local_dir):
        local_path = os.path.join(local_dir, fname)
        dropbox_path = f"{dropbox_dir}/{fname}"
        if os.path.isfile(local_path):
            upload_file(local_path, dropbox_path)

if __name__ == "__main__":
    sync_folder(LOCAL_DIR, DROPBOX_DIR)

