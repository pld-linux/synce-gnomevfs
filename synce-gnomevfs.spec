Summary:	GnomeVFS module for accessing Windows CE and Pocket PC Devices.
Name:		synce-gnomevfs
Version:	0.9.0
Release:	0.2
License:	MIT
Source0: 	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	1fa8d653297331479edcd5d983a0f75e
Group:		Applications/Communications
Vendor:		The SynCE Project
URL:		http://synce.sourceforge.net/
BuildRequires:	synce-devel = %{version}
Requires:	synce
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE-GnomeVFS is part of the SynCE project:

  http://synce.sourceforge.net/

%prep
%setup -q 

%build
%configure
%{__make}

%install
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/gnome-vfs-2.0/modules/libsyncevfs.so
%{_libdir}/gnome-vfs-2.0/modules/libsyncevfs.la
%{_sysconfdir}/gnome-vfs-2.0/modules/synce-module.conf
%{_bindir}/synce-in-computer-folder
%{_datadir}/pixmaps/synce/synce-color.png
%{_datadir}/synce/synce-in-computer-folder.sh
