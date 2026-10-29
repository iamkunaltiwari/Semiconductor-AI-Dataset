from extractors.rtl_extractor import save_rtl_metadata
# from extractors.spice_extractor import save_spice_metadata
# from extractors.layout_extractor import save_layout_metadata
# from extractors.metadata_extractor import merge_metadata


def main():
    print("=" * 60)
    print("SEMICONDUCTOR AI DATASET PIPELINE")
    print("=" * 60)

    print("\n[1/4] RTL Extraction...")
    save_rtl_metadata()

    # print("\n[2/4] SPICE Extraction...")
    # save_spice_metadata()

    # print("\n[3/4] Layout Extraction...")
    # save_layout_metadata()

    # print("\n[4/4] Merge Metadata...")
    # merge_metadata()

    print("\nPipeline Completed Successfully!")


if __name__ == "__main__":
    main()