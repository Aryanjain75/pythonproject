import instaloader
import zipfile
import os
import shutil


def download_instagram_data(username, download_high_quality=False):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    try:
        # Retrieve the profile details of the user
        profile = instaloader.Profile.from_username(L.context, username)

        # Create a directory to store the downloaded files
        if not os.path.isdir(username):
            os.makedirs(username)

        # Download all posts
        print("Downloading posts...")
        if download_high_quality:
            L.download_profile(username, profile_pic=False, download_stories=False,
                               high_quality=True)
        else:
            L.download_profile(username, profile_pic=False, download_stories=False)

        # Download all stories
        print("Downloading stories...")
        L.download_stories([profile.userid], filename_target=f'{username}/story')

        # Create a zip file to store all downloaded files
        zip_filename = f'{username}.zip'
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            # Add posts to the zip file
            for filename in os.listdir(username):
                if not filename.startswith('story'):
                    zipf.write(f'{username}/{filename}')

            # Add stories to the zip file
            for filename in os.listdir('.'):
                if filename.startswith('story'):
                    zipf.write(filename)

        # Remove the downloaded files
        for filename in os.listdir(username):
            os.remove(f'{username}/{filename}')
        os.rmdir(username)
        for filename in os.listdir('.'):
            if filename.startswith('story'):
                os.remove(filename)

        print(f"Download completed. All files are saved in '{zip_filename}'.")

    except instaloader.exceptions.ProfileNotExistsException:
        print("User does not exist.")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print("Private user account. Unable to download posts.")


def extract_instagram_data(username):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    try:
        # Login to Instagram
        L.login("aryanjain5754", "Aryanj@7725")  # Replace with your Instagram login credentials

        # Retrieve the profile details of the user
        profile = instaloader.Profile.from_username(L.context, username)

        # Print user information
        print("Username:", profile.username)
        print("Full Name:", profile.full_name)
        print("Bio:", profile.biography)
        print("Followers:", profile.followers)
        print("Following:", profile.followees)
        print("Is Private Account:", profile.is_private)

        # Retrieve and print the user's posts
        # print("Posts:")
        # try:
        #     for post in profile.get_posts():
        #         print("  -", post.url)
        # except:
        #     print("Error occurred while retrieving posts.")
        #
        # # Retrieve and print the user's tagged posts
        # print("Tagged Posts:")
        # try:
        #     for tagged_post in profile.get_tagged_posts():
        #         print("  -", tagged_post.url)
        # except:
        #     print("Error occurred while retrieving tagged posts.")

        # Prompt the user to download Instagram data
        choice = input("Do you want to download the Instagram data? (y/n): ")
        if choice.lower() == 'y':
            download_high_quality = input("Download high-quality images? (y/n): ")
            download_instagram_data(username, download_high_quality.lower() == 'y')
        else:
            print("Instagram data download skipped.")

    except instaloader.exceptions.ProfileNotExistsException:
        print("User does not exist.")


if __name__ == '__main__':
    username = input("Enter Instagram username: ")
    extract_instagram_data(username)
